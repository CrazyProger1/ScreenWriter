import os

from loguru import logger

from app.documents import create_document
from app.exceptions import (
    DocumentSavingError,
    catch_error,
    ScreenWriterError,
    SetupError,
    ClipboardEmptyError,
    KeyboardError,
    DocumentError
)
from app.keyboard import Keyboard
from app.settings import SettingsSchema
from app.utils import clipboard, observer
from config import SETTINGS_FILE, DOCUMENT_CLASSES


class ScreenWriter:
    task_header_added = observer.Event()
    screenshot_added = observer.Event()
    text_form_clipboard_pasted = observer.Event()
    document_cleared = observer.Event()
    setup = observer.Event()
    error_occurred = observer.Event()
    critical_error_occurred = observer.Event()
    reset_settings = observer.Event()

    def __init__(self, settings: SettingsSchema):
        self._settings = settings
        self._keyboard = Keyboard(self._settings)

        self._document = None

        self._screen_number = 0
        self._task_number = 0

    def _initialize_document(self):
        self._document = create_document(
            doctype=self._settings.document.doctype,
            file=self._settings.document.out_file
        )

        if not self._document:
            raise DocumentError(
                f'Document type {self._settings.document.doctype} is invalid. Supported types: '
                f'{", ".join(DOCUMENT_CLASSES.keys())}')
        self._setup_document()
        logger.info('Document initialized')

    @catch_error(ScreenWriterError, error_occurred)
    def _setup_document(self):
        try:
            if self._settings.document.create_new_file:
                self._document.clear()

            self._document.stylize(
                font=self._settings.style.font,
                font_size=self._settings.style.font_size
            )
        except Exception as e:
            raise ScreenWriterError(
                'An error occurred while trying to stylize the document. Check if your style is correct'
            )

    @catch_error(ScreenWriterError, error_occurred)
    def _add_task_header(self):
        self._task_number += 1
        text = self._settings.text.task_header.format(number=self._task_number)
        self._document.add_header(text)
        self.task_header_added(self._task_number)

    @catch_error(ScreenWriterError, error_occurred)
    def _add_screenshot(self):
        try:
            clipboard.clear()

            file = self._settings.others.temp_image_file
            if os.path.isfile(file):
                os.remove(file)

            clipboard.save_screenshot(file)
            self._document.add_picture(file)
            self._screen_number += 1
            self._document.add_text(self._settings.text.caption.format(number=self._screen_number), center=True)
            if os.path.isfile(file):
                os.remove(file)

            self.screenshot_added(self._screen_number)
        except Exception as e:
            raise ScreenWriterError(
                'An error occurred while trying to grab screenshot from clipboard. Please try again')

    @catch_error(ScreenWriterError, error_occurred)
    def _paste_text_from_clipboard(self):
        text = clipboard.read()
        if text:
            self._document.add_text(text)
            self.text_form_clipboard_pasted(text)
        else:
            raise ClipboardEmptyError('Clipboard is empty')

    @catch_error(ScreenWriterError, error_occurred)
    def _clear_document(self):
        self._document.clear()
        self._task_number = 0
        self._screen_number = 0
        self.document_cleared()

    @catch_error(ScreenWriterError, error_occurred)
    def _setup(self):
        try:
            os.system(f'start notepad {SETTINGS_FILE}')
        except Exception as e:
            raise SetupError('Failed to open the settings file. Please try again')
        self.setup()

    @catch_error(ScreenWriterError, error_occurred)
    def _try_save(self):
        try:
            self._document.save()
        except PermissionError:
            raise DocumentSavingError(
                message='An error occurred while trying to save file. Check that the file is closed'
            )

    @catch_error(ScreenWriterError, error_occurred)
    def _on_shortcut_pressed(self, shortcut: str):
        shortcuts = self._settings.shortcuts

        handlers = {
            shortcuts.screenshot_shortcut: self._add_screenshot,
            shortcuts.setup_shortcut: self._setup,
            shortcuts.add_task_header_shortcut: self._add_task_header,
            shortcuts.clear_document_shortcut: self._clear_document,
            shortcuts.paste_text_from_clipboard_shortcut: self._paste_text_from_clipboard
        }

        handler = handlers.get(shortcut)

        if handler:
            handler()

        self._try_save()

    @catch_error(ScreenWriterError, error_occurred)
    def run(self):
        try:
            self._initialize_document()

            self._keyboard.shortcut_pressed.add_listener(self._on_shortcut_pressed)
            self._keyboard.error_occurred.add_listener(self.error_occurred)
            self._keyboard.reset_settings.add_listener(self.reset_settings)

            try:
                self._keyboard.listen()
            except KeyboardInterrupt:
                pass
            except KeyboardError as e:
                raise ScreenWriterError(e.message)

            self._try_save()
        except DocumentError as e:
            self._setup()
            self.critical_error_occurred(e)
        except ScreenWriterError:
            raise
        except Exception as e:
            self.critical_error_occurred(e)
