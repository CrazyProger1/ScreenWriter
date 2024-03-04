import logging

from src.core.config import APP
from src.core.types import (
    BaseDocumentManager,
    BaseComponent
)

logger = logging.getLogger(APP)


class DocumentManager(BaseDocumentManager):
    def open_document(self, file: str):
        logger.info(f'Document opened: {file}')

    def clear_document(self):
        pass

    @property
    def content(self) -> str:
        return ''

    def add_component(self, component: BaseComponent):
        pass
