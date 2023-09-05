from abc import ABC, abstractmethod
from app.settings import SettingsSchema
from app.logic import ScreenWriter
from app.utils import cli
from app.cli.msgs import StatusMessage, ShortcutHelpMessage
from app.cli.theme import ThemeSchema
from config import APP, VERSION


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

    def print_welcome(self):
        cli.print_colored(f'{APP} - V{VERSION}', color=self._theme.welcome_text_style)

    def print_bye(self):
        cli.print_status(StatusMessage.terminating.value)

    def print_help(self):
        print()
        shortcuts = self._settings.shortcuts

        for name, shortcut in shortcuts.__dict__.items():
            cli.print_info(getattr(ShortcutHelpMessage, name).value.format(shortcut=shortcut))
        print()

    def print_screenshot_saved(self, number: int):
        cli.print_status(StatusMessage.screenshot_saved.value.format(number=number))

    def print_task_header_added(self, number: int):
        cli.print_status(StatusMessage.task_header_added.value.format(number=number))

    def print_text_pasted(self, text: str):
        cli.print_status(StatusMessage.text_pasted.value)
        print()
        cli.print_raw(text)

    def print_document_cleared(self):
        cli.print_status(StatusMessage.document_cleared.value)

    def _register_listeners(self):
        ScreenWriter.screenshot_added.add_listener(self.print_screenshot_saved)
        ScreenWriter.task_header_added.add_listener(self.print_task_header_added)
        ScreenWriter.text_form_clipboard_pasted.add_listener(self.print_text_pasted)
        ScreenWriter.document_cleared.add_listener(self.print_document_cleared)

    def show(self):
        self._register_listeners()
        self.print_welcome()
        self.print_help()

    def destroy(self):
        self.print_bye()
