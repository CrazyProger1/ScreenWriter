import logging

from app.utils import settings
from app import documents

APP = 'SCREEN WRITER'
VERSION = '0.2'

SETTINGS_FILE = 'settings.toml'
SETTINGS_FMT = settings.Format.TOML
RESET_SETTINGS_SHORTCUT = 'Ctrl + R'

DOCUMENT_CLASSES = {
    'docx': documents.DocxDocument
}

LOGGING_VERBOSITY = False
LOG_FILE = f'{APP.replace(" ", "_").lower()}_{VERSION}.log'
LOGGING_LEVEL = logging.INFO
