import keyboard

from app.settings import SettingsSchema
from app.utils import observer


class Keyboard:
    shortcut_pressed = observer.Event()

    def __init__(self, settings: SettingsSchema):
        self._settings = settings
        self._register_hotkeys()

    def _register_hotkeys(self):
        for shortcut in self._settings.shortcuts.__dict__.values():
            keyboard.add_hotkey(
                shortcut,
                self.shortcut_pressed,
                args=(shortcut, )
            )

    def listen(self):
        keyboard.wait(self._settings.shortcuts.exit_shortcut)
