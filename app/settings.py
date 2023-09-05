from app.utils import settings


class ShortcutsSchema(settings.SettingsSchema):
    exit_shortcut: str = 'Ctrl + Q'
    add_task_header_shortcut: str = 'Ctrl + Space'
    paste_text_from_clipboard_shortcut: str = 'Ctrl + Shift + V'
    clear_document_shortcut: str = 'Ctrl + Shift + P'
    setup_shortcut: str = 'Ctrl + Shift + S'
    screenshot_shortcut: str = 'Shift + Windows + S'


class SettingsSchema(settings.SettingsSchema):
    doctype: str = 'docx'
    out_file: str = 'out.docx'
    create_new_file: bool = False
    temp_image_file: str = 'temp.png'
    font: str = 'Times New Roman'
    font_size: int = 14
    caption: str = 'Рис.'
    task_header: str = 'Завдання №'

    shortcuts: ShortcutsSchema


