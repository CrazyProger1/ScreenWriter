import logging

from pydantic import BaseModel

from src.core.config import APP
from src.core.events import MainChannel

logger = logging.getLogger(APP)


class Core:
    def __init__(self, arguments: BaseModel, settings: BaseModel, context: BaseModel):
        self._arguments = arguments
        self._settings = settings
        self._context = context

        self._running = True

        logger.info('Core initialized')

    def _mainloop(self):
        try:
            while self._running:
                pass
        except KeyboardInterrupt:
            pass

    def run(self):
        logger.info('Core started')

        self._mainloop()

        MainChannel.terminated.publish()
