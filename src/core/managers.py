import logging

from src.core.config import APP
from src.core.types import (
    BaseDocumentManager,
    BaseComponent, BaseStyle
)

logger = logging.getLogger(APP)


class DocumentManager(BaseDocumentManager):
    def open_document(self, file: str):
        logger.debug(f'Document loaded: {file}')

    def clear_document(self):
        logger.debug('Document cleared')

    def add_component(self, component: BaseComponent):
        logger.debug(f'Component added: {component}')

    def stylize(self, style: BaseStyle):
        logger.debug(f'Styles applied: {style}')

    @property
    def content(self) -> str:
        return ''
