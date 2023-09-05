from app.app import App
from app.keyboard import Keyboard
from config import SETTINGS_FILE


class CLI(App):

    def run(self):
        def on_shortcut_pressed(shortcut):
            print(shortcut)

        Keyboard.shortcut_pressed.add_listener(on_shortcut_pressed)

        self._keyboard.listen()
        self._settings_loader.save(SETTINGS_FILE, self.settings)
