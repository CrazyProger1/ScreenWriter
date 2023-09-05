from app.utils import settings
from app.cli import printers
from app import documents

APP = 'SCREEN WRITER'
VERSION = '0.2'

SETTINGS_FILE = 'settings.toml'
SETTINGS_FMT = settings.Format.TOML

PRINTER_CLASS = printers.BasePrinter
DOCUMENT_CLASSES = {
    'docx': documents.DocxDocument
}
