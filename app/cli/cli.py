from config import SETTINGS_FILE, PRINTER_CLASS

from app.app import App
from app.keyboard import Keyboard
from .printers import Printer


class CLI(App):
    def __init__(self, *args, **kwargs):
        super(CLI, self).__init__(*args, **kwargs)
        self._printer: Printer = PRINTER_CLASS(self.settings)
        Keyboard.shortcut_pressed.add_listener(self._on_shortcut_pressed)

    def _on_shortcut_pressed(self, shortcut: str):
        shortcuts = self.settings.shortcuts

        match shortcut:
            case shortcuts.screenshot_shortcut:
                self._printer.print_status('screenshot_saved')

    def run(self):
        self._printer.print_welcome()
        self._printer.print_help()

        self._keyboard.listen()
        self._settings_loader.save(SETTINGS_FILE, self.settings)
