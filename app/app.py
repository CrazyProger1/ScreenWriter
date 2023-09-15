import argparse
from time import sleep

from app.logic import ScreenWriter
from app.utils import settings
from app.settings import SettingsSchema
from app.utils.exceptions import SettingsDecodeError
from config import SETTINGS_FILE, SETTINGS_FMT


class App:
    """App facade"""

    def __init__(self, clargs: argparse.Namespace):
        self._args = clargs
        self._settings_loader = settings.create_loader(SETTINGS_FMT, SettingsSchema)
        self._settings: SettingsSchema | None = None

        self._load_settings()

        self._worker = ScreenWriter(
            settings=self.settings
        )
        self._worker.reset_settings.add_listener(self.reset_settings)

    def _load_settings(self):
        try:
            self._settings = self._settings_loader.load(SETTINGS_FILE)
        except (FileNotFoundError, SettingsDecodeError):
            self._settings = SettingsSchema()
            self._settings_loader.save(SETTINGS_FILE, self._settings)

    @property
    def settings(self) -> SettingsSchema:
        return self._settings

    @property
    def args(self) -> argparse.Namespace:
        return self._args

    def reset_settings(self):
        self._settings = SettingsSchema()
        self._settings_loader.save(SETTINGS_FILE, self._settings)

    @staticmethod
    def _on_critical_error(e):
        for i in range(5, 0, -1):
            print('.' * i)
            sleep(1)

    def run(self):
        self._worker.critical_error_occurred.add_listener(self._on_critical_error)
        self._worker.run()
        # self._settings_loader.save(SETTINGS_FILE, self.settings)
