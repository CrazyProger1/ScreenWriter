from app.utils import settings
from app.cli import printers

APP = 'SCREEN WRITER'
VERSION = '0.2'

SETTINGS_FILE = 'settings.toml'
SETTINGS_LOADER_CLASS = settings.TOMLSettingsLoader

PRINTER_CLASS = printers.BasePrinter
