import argparse

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

    def run(self):
        self._worker.run()
        self._settings_loader.save(SETTINGS_FILE, self.settings)
