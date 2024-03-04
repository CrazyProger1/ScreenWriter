import logging


from pydantic import BaseModel

from src.core.config import APP
from src.core.events import MainChannel
from src.core.types import BaseDocumentManager
from src.core.styles import CommonStyle
from src.core.components import (
    Image,
    Header
)

from src.utils.keyboard import BaseKeyboardManager
from src.utils.clipboard import (
    read,
    save_image,
    clear
)

logger = logging.getLogger(APP)


class Core:
    def __init__(
            self,
            arguments: BaseModel,
            settings: BaseModel,
            context: BaseModel,
            kbd_manager: BaseKeyboardManager,
            doc_manager: BaseDocumentManager
    ):
        self._arguments = arguments
        self._settings = settings
        self._context = context
        self._kbd_manager = kbd_manager
        self._doc_manager = doc_manager

        self._running = True

        self._init_document()

        logger.info('Core initialized')

    def _init_document(self):
        self._doc_manager.open_document(self._settings.document.current_document)
        self._doc_manager.stylize(CommonStyle(
            font=self._settings.style.font,
            font_size=self._settings.style.font_size
        ))

    def _mainloop(self):
        try:
            while self._running:
                pass
        except KeyboardInterrupt:
            pass

    def _handle_screenshot(self):
        logger.debug('Handling screenshot')
        path = self._settings.other.temporary_file
        save_image(path)
        clear()

        self._context.screenshot_counter += 1
        self._doc_manager.add_component(
            Image(
                path=path,
                caption=self._settings.style.caption_format.format(number=self._context.screenshot_counter)
            )
        )
        MainChannel.screenshot_taken.publish()

    def _handle_task_header(self):

        self._context.task_counter += 1
        self._doc_manager.add_component(
            Header(
                text=self._settings.style.task_header_format.format(number=self._context.task_counter)
            )
        )
        MainChannel.task_header_added.publish()

    def _register_keyboard_handlers(self):
        shortcuts = self._settings.shortcuts

        self._kbd_manager.add_callback(shortcuts.screenshot, self._handle_screenshot)
        self._kbd_manager.add_callback(shortcuts.add_task_header, self._handle_task_header)

    def run(self):
        logger.info('Core started')

        self._register_keyboard_handlers()

        self._mainloop()

        MainChannel.terminated.publish()
