import os

from app.keyboard import Keyboard
from app.documents import create_document
from app.settings import SettingsSchema
from app.utils import clipboard, observer


class ScreenWriter:
    task_header_added = observer.Event()
    screenshot_added = observer.Event()
    text_form_clipboard_pasted = observer.Event()
    document_cleared = observer.Event()
    setup = observer.Event()

    def __init__(self, settings: SettingsSchema):
        self._settings = settings
        self._keyboard = Keyboard(self._settings)
        self._document = create_document(
            doctype=self._settings.document.doctype,
            file=self._settings.document.out_file
        )

        self._setup_document()

        self._screen_number = 0
        self._task_number = 0

    def _setup_document(self):
        if self._settings.document.create_new_file:
            self._document.clear()

        self._document.stylize(
            font=self._settings.style.font,
            font_size=self._settings.style.font_size
        )

    def _add_task_header(self):
        self._task_number += 1
        text = self._settings.text.task_header.format(number=self._task_number)
        self._document.add_header(text)
        self.task_header_added(self._task_number)

    def _add_screenshot(self):
        clipboard.clear()
        self._screen_number += 1
        file = self._settings.others.temp_image_file
        if os.path.isfile(file):
            os.remove(file)

        clipboard.save_screenshot(file)
        self._document.add_picture(file)
        self._document.add_text(self._settings.text.caption.format(number=self._screen_number), center=True)
        if os.path.isfile(file):
            os.remove(file)

        self.screenshot_added(self._screen_number)

    def _paste_text_from_clipboard(self):
        text = clipboard.read()
        self._document.add_text(text)
        self.text_form_clipboard_pasted(text)

    def _clear_document(self):
        self._document.clear()
        self._task_number = 0
        self._screen_number = 0
        self.document_cleared()

    def _setup(self):
        self.setup()

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

        self._document.save()

    def run(self):
        self._keyboard.shortcut_pressed.add_listener(self._on_shortcut_pressed)

        try:
            self._keyboard.listen()
        except KeyboardInterrupt:
            pass

        self._document.save()
