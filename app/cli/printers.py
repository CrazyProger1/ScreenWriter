from abc import ABC, abstractmethod

import colorama

from app.utils import cli
from app.settings import SettingsSchema
from app.cli.theme import ThemeSchema
from app.cli.msgs import ShortcutHelpMessage, StatusMessage

colorama.init()


class Printer(ABC):
    def __init__(self, settings: SettingsSchema, theme: ThemeSchema = ThemeSchema()):
        self._settings = settings
        self._theme = theme
        self._configure_cli_util()

    def _configure_cli_util(self):
        cli.PRINT_STYLES['status'] = self._theme.status_style
        cli.PRINT_STYLES['info'] = self._theme.info_style

    def set_theme(self, theme: ThemeSchema):
        self._theme = theme
        self._configure_cli_util()

    @abstractmethod
    def print_welcome(self):
        ...

    @abstractmethod
    def print_help(self):
        ...

    @abstractmethod
    def print_status(self, status: str, formatting: dict = None):
        ...


class BasePrinter(Printer):
    def print_welcome(self):
        from config import APP, VERSION

        cli.print_colored(f'{APP} - V{VERSION}', color=self._theme.welcome_text_style)

    def print_help(self):
        print()
        shortcuts = self._settings.shortcuts

        for name, shortcut in shortcuts.__dict__.items():
            cli.print_info(getattr(ShortcutHelpMessage, name).value.format(shortcut=shortcut))
        print()

    def print_status(self, status: str, formatting: dict = None):
        if formatting and not isinstance(formatting, dict):
            raise TypeError(f'formatting must be a dict, not {type(formatting).__name__}')

        msg = getattr(StatusMessage, status).value

        if formatting:
            msg = msg.format(**formatting)

        cli.print_status(msg)
