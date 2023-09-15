from abc import ABC, abstractmethod
from app.settings import SettingsSchema
from app.logic import ScreenWriter
from app.utils import cli
from app.cli.msgs import StatusMessage, ShortcutHelpMessage
from app.cli.theme import ThemeSchema
from app.exceptions import ScreenWriterError
from config import APP, VERSION, RESET_SETTINGS_SHORTCUT


class CLI(ABC):
    def __init__(self, settings: SettingsSchema):
        self._settings = settings

    @abstractmethod
    def show(self):
        ...

    @abstractmethod
    def destroy(self):
        ...


class BaseCLI(CLI):
    def __init__(self, *args, **kwargs):
        super(BaseCLI, self).__init__(*args, **kwargs)

        self._theme = ThemeSchema()
        self._setup_cli_utils()

    def _setup_cli_utils(self):
        cli.setup_styles(
            info=self._theme.info_style,
            status=self._theme.status_style,
        )

    def _print_welcome(self):
        cli.print_colored(f'{APP} - V{VERSION}', color=self._theme.welcome_text_style)

    @staticmethod
    def _print_bye():
        cli.print_status(StatusMessage.terminating.value)

    def _print_help(self):
        print()
        shortcuts = self._settings.shortcuts

        cli.print_info(ShortcutHelpMessage.reset_settings_shortcut.value.format(shortcut=RESET_SETTINGS_SHORTCUT))

        for name, shortcut in shortcuts.__dict__.items():
            cli.print_info(getattr(ShortcutHelpMessage, name).value.format(shortcut=shortcut))
        print()

    @staticmethod
    def _print_screenshot_saved(number: int):
        cli.print_status(StatusMessage.screenshot_saved.value.format(number=number))

    @staticmethod
    def _print_task_header_added(number: int):
        cli.print_status(StatusMessage.task_header_added.value.format(number=number))

    @staticmethod
    def _print_text_pasted(text: str):
        cli.print_status(StatusMessage.text_pasted.value)
        print()
        cli.print_raw(text)

    @staticmethod
    def _print_document_cleared():
        cli.print_status(StatusMessage.document_cleared.value)

    @staticmethod
    def _print_error(error: ScreenWriterError):
        cli.print_neg(error)

    @staticmethod
    def _print_settings_reset():
        cli.print_status(StatusMessage.settings_reset.value)

    def _register_listeners(self):
        ScreenWriter.screenshot_added.add_listener(self._print_screenshot_saved)
        ScreenWriter.task_header_added.add_listener(self._print_task_header_added)
        ScreenWriter.text_form_clipboard_pasted.add_listener(self._print_text_pasted)
        ScreenWriter.document_cleared.add_listener(self._print_document_cleared)
        ScreenWriter.error_occurred.add_listener(self._print_error)
        ScreenWriter.reset_settings.add_listener(self._print_settings_reset)

    def show(self):
        self._register_listeners()
        self._print_welcome()
        self._print_help()

    def destroy(self):
        self._print_bye()


def create_cli(settings: SettingsSchema):
    return BaseCLI(settings=settings)
