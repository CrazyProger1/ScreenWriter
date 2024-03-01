from i18n import TranslatableEnum


class Message(TranslatableEnum):
    WAITING_FOR_SCREENSHOT = 'Waiting for {shortcut}...'
    SCREENSHOT_SAVED = 'Screenshot №{number} saved to document'
    DOCUMENT_OPENED = 'New document opened'
    TERMINATING = 'Terminating...'
