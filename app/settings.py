from app.utils import settings


class ShortcutsSettingsSchema(settings.SettingsSchema):
    exit_shortcut: str = 'Ctrl + Q'
    add_task_header_shortcut: str = 'Ctrl + Space'
    paste_text_from_clipboard_shortcut: str = 'Ctrl + Shift + V'
    clear_document_shortcut: str = 'Ctrl + Shift + P'
    setup_shortcut: str = 'Ctrl + Shift + S'
    screenshot_shortcut: str = 'Shift + Windows + S'


class DocumentSettingsSchema(settings.SettingsSchema):
    doctype: str = 'docx'
    out_file: str = 'out.docx'
    create_new_file: bool = False


class StyleSettingsSchema(settings.SettingsSchema):
    font: str = 'Times New Roman'
    font_size: int = 14


class TextSettingsSchema(settings.SettingsSchema):
    caption: str = 'Рис.{number}'
    task_header: str = 'Завдання №{number}'


class OthersSettingsSchema(settings.SettingsSchema):
    temp_image_file: str = 'temp.png'


class SettingsSchema(settings.SettingsSchema):
    text: TextSettingsSchema = TextSettingsSchema()
    others: OthersSettingsSchema = OthersSettingsSchema()
    style: StyleSettingsSchema = StyleSettingsSchema()
    document: DocumentSettingsSchema = DocumentSettingsSchema()
    shortcuts: ShortcutsSettingsSchema = ShortcutsSettingsSchema()
