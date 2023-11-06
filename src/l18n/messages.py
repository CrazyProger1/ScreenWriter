from enum import Enum


class ErrorMessages(str, Enum):
    ABC = 'ABC'


class Messages(str, Enum):
    welcome = '{app} - V{ver}'


class StatusMessages(str, Enum):
    terminating = 'Terminating...'
    task_header_added = 'Task header  №{number} added'
    text_pasted = 'Text pasted'
    document_cleared = 'Document cleared'
    screenshot_saved = 'Screenshot №{number} saved'
    settings_reset = 'Settings reset successfully'


class HelpMessages(str, Enum):
    pass
