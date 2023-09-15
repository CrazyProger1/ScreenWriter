import keyboard

from config import RESET_SETTINGS_SHORTCUT

from app.settings import SettingsSchema
from app.utils import observer
from app.exceptions import KeyboardError, catch_error


class Keyboard:
    shortcut_pressed = observer.Event()
    error_occurred = observer.Event()
    reset_settings = observer.Event()

    def __init__(self, settings: SettingsSchema):
        self._settings = settings

    @catch_error(KeyboardError, error_occurred)
    def _register_hotkeys(self):
        keyboard.add_hotkey(RESET_SETTINGS_SHORTCUT, self.reset_settings)

        for shortcut in self._settings.shortcuts.__dict__.values():
            try:
                keyboard.add_hotkey(
                    shortcut,
                    self.shortcut_pressed,
                    args=(shortcut,)
                )
            except ValueError as e:
                raise KeyboardError(
                    f'Shortcut {shortcut} is invalid. '
                    f'Shortcuts must be in the format: Key + Key. '
                    f'Try fixing this in settings'
                )

    def listen(self):
        self._register_hotkeys()
        keyboard.wait(self._settings.shortcuts.exit_shortcut)
