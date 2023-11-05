import os

import pyperclip
from loguru import logger

from src.utils import keyboard, clipboard, observer
from src.context import Context
from src.document import get_manager, Doctype

from config import (
    RESET_SETTINGS_SHORTCUT,
    LOG_FILE
)


class Core:
    screenshot_event = observer.Event()
    exit_event = observer.Event()
    open_logfile_event = observer.Event()
    open_document_event = observer.Event()
    open_settings_event = observer.Event()
    clear_document_event = observer.Event()

    invalid_doctype_error_event = observer.Event()
    permission_denied_error_event = observer.Event()

    def __init__(self, context: Context):
        self._context = context
        self._stop = False

        self._settings = self._context.settings
        self._docsettings = self._settings.document
        self._outfile = self._settings.document.out_file

        self._shortcut_manager = keyboard.ShortcutManager()
        self._document_manager = get_manager(doctype=self._docsettings.doctype)

        if not self._document_manager:
            self.invalid_doctype_error_event(self._docsettings.doctype)
            self._document_manager = get_manager(doctype=Doctype.DOCX)

        self._picture_counter = 0
        self._tasks_counter = 0

    def _open_document(self):
        if self._docsettings.create_new_file:
            self._document_manager.create(self._outfile)
        else:
            try:
                self._document_manager.open(self._outfile)
            except FileNotFoundError:
                self._document_manager.create(self._outfile)

    def _save_document(self):
        try:
            self._document_manager.save(self._outfile)
        except PermissionError:
            self.permission_denied_error_event()

    def _register_shortcuts(self):
        shortcuts = self._context.settings.shortcuts
        handlers = {
            shortcuts.screenshot_shortcut: self._on_screenshot,
            shortcuts.exit_shortcut: self._on_exit,
            shortcuts.open_logfile_shortcut: self._on_open_logfile,
            shortcuts.clear_document_shortcut: self._on_clear_document,
            shortcuts.open_document_shortcut: self._on_open_document,
            shortcuts.open_settings_shortcut: self._on_open_settings,
            shortcuts.add_task_header_shortcut: self._on_add_task_header,
            shortcuts.paste_text_from_clipboard_shortcut: self._on_paste_text,
            shortcuts.paste_picture_from_clipboard_shortcut: self._on_paste_picture,
            RESET_SETTINGS_SHORTCUT: self._on_reset_settings,

        }

        for shortcut, handler in handlers.items():
            self._shortcut_manager.register(shortcut, handler)

    def _open_file_via_notepad(self, file: str):
        os.system(f'notepad {file}')

    def _run_file(self, file: str):
        os.system(f'start {file}')

    def _on_screenshot(self):
        self._picture_counter += 1

    def _on_exit(self):
        self._stop = True

    def _on_open_logfile(self):
        self._open_file_via_notepad(LOG_FILE)

    def _on_clear_document(self):
        self._document_manager.clear()

    def _on_open_document(self):
        self._run_file(self._docsettings.out_file)

    def _on_open_settings(self):
        self._open_file_via_notepad(self._context.arguments.settings)

    def _on_reset_settings(self):
        self._context.reset_settings()

    def _on_add_task_header(self):
        self._tasks_counter += 1

    def _on_paste_text(self):
        self._document_manager.add_paragraph(pyperclip.paste())
        self._save_document()

    def _on_paste_picture(self):
        self._picture_counter += 1
        file = self._settings.others.temp_image_file
        caption = self._settings.text.caption.format(number=self._picture_counter)
        clipboard.save_screenshot(file)
        self._document_manager.add_picture(file, caption=caption)
        self._save_document()

    def run(self):
        self._open_document()
        self._register_shortcuts()
        try:
            while not self._stop:
                pass
        except KeyboardInterrupt:
            pass

        logger.info('Application succesefully terminated')
