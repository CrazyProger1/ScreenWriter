import logging

import colorama
from art import text2art
from pydantic import BaseModel

from src.core.config import APP, TITLE
from src.core.events import MainChannel
from src.utils.cli import (
    print_info,
    print_positive,
    print_negative,
    print_colored
)

from .enums import Message
from ..types import BaseUI
from ..enums import GraphicMode

logger = logging.getLogger(APP)


class CLI(BaseUI):
    mode = GraphicMode.CLI

    def __init__(self, arguments: BaseModel, settings: BaseModel, context: BaseModel):
        self._arguments = arguments
        self._settings = settings
        self._context = context
        logger.info('CLI initialized')

    def _print_welcome(self):
        print_colored(text2art(APP), color=colorama.Fore.LIGHTMAGENTA_EX)

    def _print_waiting(self):
        print_info(Message.WAITING_FOR_SCREENSHOT)

    def _print_help(self):
        pass

    def _handle_screenshot_taken(self):
        print_positive(Message.SCREENSHOT_SAVED.format(number=self._context.screenshot_counter))

    def _handle_document_opened(self):
        print_positive(Message.DOCUMENT_OPENED)

    def _handle_document_started(self):
        pass

    def _handle_new_document_created(self):
        pass

    def _handle_terminated(self):
        print_info(Message.TERMINATING)

    def run(self):
        logger.info('CLI started')
        self._print_welcome()

        MainChannel.screenshot_taken.subscribe(self._handle_screenshot_taken)
        MainChannel.document_opened.subscribe(self._handle_document_opened)
        MainChannel.document_started.subscribe(self._handle_document_started)
        MainChannel.new_document_created.subscribe(self._handle_new_document_created)
        MainChannel.terminated.subscribe(self._handle_terminated)

        self._print_help()
        self._print_waiting()
