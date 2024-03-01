import logging
import typeguard

APP = 'ScreenWriter'
VERSION = '0.0.3'
TITLE = f'ScreenWriter-V{VERSION}'
DEBUG = True

if not DEBUG:
    typeguard.typechecked = lambda x: x

DEFAULT_SETTINGS_FILE = 'settings.toml'

LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
