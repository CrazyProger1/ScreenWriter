import os

from config import SETTINGS_FILE

from app.app import App
from app.keyboard import Keyboard
from app.cli.printers import create_printer
from app.documents import create_document
from app.utils import clipboard


class CLI(App):
    def __init__(self, *args, **kwargs):
        super(CLI, self).__init__(*args, **kwargs)
        self._printer = create_printer(self.settings)
        self._document = create_document(self.settings.doctype, self.settings.out_file)

        if self.settings.create_new_file:
            self._document.clear()

        Keyboard.shortcut_pressed.add_listener(self._on_shortcut_pressed)

        self._tasks_counter = 0
        self._screenshots_counter = 0

    def _add_task_header(self):
        self._tasks_counter += 1
        text = self.settings.task_header.format(number=self._tasks_counter)
        self._document.add_header(text)
        self._printer.print_header_added(self._tasks_counter)

    def _add_screenshot(self):
        clipboard.clear()
        self._screenshots_counter += 1
        file = self.settings.temp_image_file
        if os.path.isfile(file):
            os.remove(file)

        clipboard.save_screenshot(file)
        self._document.add_picture(file)
        self._document.add_text(self.settings.caption.format(number=self._screenshots_counter), center=True)
        if os.path.isfile(file):
            os.remove(file)
        self._printer.print_screenshot_saved(self._screenshots_counter)

    def _paste_text_from_clipboard(self):
        text = clipboard.read()
        self._document.add_text(text)
        self._printer.print_text_pasted()

    def _clear_document(self):
        self._document.clear()
        self._tasks_counter = 0
        self._screenshots_counter = 0

    def _setup(self):
        pass

    def _on_shortcut_pressed(self, shortcut: str):
        shortcuts = self.settings.shortcuts

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
        self._printer.print_welcome()
        self._printer.print_help()

        try:
            self._keyboard.listen()
        except KeyboardInterrupt:
            pass
        self._printer.print_bye()
        self._settings_loader.save(SETTINGS_FILE, self.settings)
