import colorama

from src.context import Context
from src.events import (
    CoreEventChannel
)
from src.utils import cli
from src.l18n import (
    set_language,
    _,
    StatusMessages,
    Messages
)

from config import (
    APP,
    VER
)


class CLI:
    def __init__(self, context: Context):
        self._context = context

        set_language(self._context.settings.interface.language)

        cli.set_style('status', colorama.Fore.LIGHTGREEN_EX)

    def _register_event_handlers(self):
        CoreEventChannel.screenshot_event.add_listener(self._on_screenshot)
        CoreEventChannel.exit_event.add_listener(self._on_exit)

    def _print_welcome(self):
        cli.print_colored(_(Messages.welcome).format(app=APP.upper(), ver=VER), color=colorama.Fore.LIGHTBLUE_EX)

    def _on_screenshot(self, number):
        cli.print_status(_(StatusMessages.screenshot_saved).format(number=number))

    def _on_exit(self):
        cli.print_status(_(StatusMessages.terminating))

    def run(self):
        self._register_event_handlers()
        self._print_welcome()
