from enum import Enum


class ShortcutHelpMessage(str, Enum):
    reset_settings_shortcut = 'Press {shortcut} to reset settings (always works)'
    exit_shortcut = 'Press {shortcut} to exit'
    add_task_header_shortcut = 'Press {shortcut} to add task header'
    paste_text_from_clipboard_shortcut = 'Press {shortcut} to paste text from clipboard'
    clear_document_shortcut = 'Press {shortcut} to clear document'
    setup_shortcut = 'Press {shortcut} to setup program'
    screenshot_shortcut = 'Waiting for {shortcut}...'


class StatusMessage(str, Enum):
    terminating = 'Terminating...'
    task_header_added = 'Task header  №{number} added'
    text_pasted = 'Text pasted'
    document_cleared = 'Document cleared'
    screenshot_saved = 'Screenshot №{number} saved'
    settings_reset = 'Settings reset successfully'
