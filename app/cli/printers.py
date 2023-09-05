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
    def print_text_pasted(self):
        ...

    @abstractmethod
    def print_header_added(self, number: int):
        ...

    @abstractmethod
    def print_screenshot_saved(self, number: int):
        ...

    @abstractmethod
    def print_bye(self):
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

    def print_text_pasted(self):
        cli.print_status(StatusMessage.text_pasted.value)

    def print_header_added(self, number: int):
        cli.print_status(StatusMessage.task_header_added.value.format(number=number))

    def print_screenshot_saved(self, number: int):
        cli.print_status(StatusMessage.screenshot_saved.value.format(number=number))

    def print_bye(self):
        cli.print_status(StatusMessage.exit.value)


def create_printer(settings: SettingsSchema, theme: ThemeSchema = ThemeSchema()) -> Printer:
    from config import PRINTER_CLASS
    return PRINTER_CLASS(settings=settings, theme=theme)
