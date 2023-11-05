import logging

# App
APP = 'Screen Writer'
VERSION = VER = '0.3'
DESCRIPTION = 'ScreenWriter is a simple util that makes your daily life at university easier.'
DEBUG = False

# Logging
LOGGING_VERBOSITY = True
LOG_FILE = f'{APP.replace(" ", "_").lower()}_{VERSION}.log'
LOGGING_LEVEL = logging.INFO

# L18N
LOCALEDIR = 'res/locales'
DEFAULT_LANGUAGE = 'en'

# Settings
DEFAULT_SETTINGS_FILE = 'settings.toml'
RESET_SETTINGS_SHORTCUT = 'Ctrl + Shift + R'

if not DEBUG:
    import typeguard

    typeguard.typechecked = lambda func: func
