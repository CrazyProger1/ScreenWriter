from app.utils import settings
from app import documents

APP = 'SCREEN WRITER'
VERSION = '0.2'

SETTINGS_FILE = 'settings.toml'
SETTINGS_FMT = settings.Format.TOML

DOCUMENT_CLASSES = {
    'docx': documents.DocxDocument
}
