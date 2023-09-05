import argparse
import os
from abc import ABC, abstractmethod

from app.settings import SettingsSchema
from app.utils.exceptions import SettingsDecodeError
from app.keyboard import Keyboard

from config import SETTINGS_FILE, SETTINGS_LOADER


class App(ABC):
    def __init__(self, args: argparse.Namespace):
        self._args = args
        self._settings_loader = SETTINGS_LOADER(SettingsSchema)
        self._settings: SettingsSchema | None = None

        self._load_settings()
        self._keyboard = Keyboard(self._settings)

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

    @abstractmethod
    def run(self):
        ...
