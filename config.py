import logging

# App
APP = 'Screen Writer'
VERSION = VER = '0.3'
DESCRIPTION = 'ScreenWriter is a simple util that makes your daily life at university easier.'
DEBUG = True

# Logging
LOGGING_VERBOSITY = True
LOG_FILE = f'{APP.replace(" ", "_").lower()}_{VERSION}.log'
LOGGING_LEVEL = logging.INFO

# L18N
LOCALEDIR = 'res/locales'
DEFAULT_LANGUAGE = 'en'

# Settings
RESET_SETTINGS_SHORTCUT = 'Ctrl + Shift + R'
