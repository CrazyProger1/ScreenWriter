import argparse

from src.utils import settings

from src.settings import SettingsSchema
from src.arguments import parse_arguments


class Context:
    def __init__(self, **kwargs):
        self._arguments = kwargs.pop('arguments', None)
        self._settings: SettingsSchema | None = kwargs.pop('settings', None)

        if not self._arguments:
            self._arguments = parse_arguments()

        if not self._settings:
            self.load_settings()

    def load_settings(self):
        file = self.arguments.settings
        try:
            self._settings = settings.load(
                schema=SettingsSchema,
                file=file
            )
        except (FileNotFoundError, settings.exceptions.SettingsError):
            self.reset_settings()

    def reset_settings(self):
        self._settings = SettingsSchema()
        self.save_settings()

    def save_settings(self):
        file = self.arguments.settings
        settings.save(
            instance=self._settings,
            file=file
        )

    @property
    def settings(self) -> SettingsSchema:
        return self._settings

    @property
    def arguments(self) -> argparse.Namespace:
        return self._arguments
