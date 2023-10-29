from pydantic import BaseModel


class ShortcutsSettingsSchema(BaseModel):
    exit_shortcut: str = 'Ctrl + Q'
    add_task_header_shortcut: str = 'Ctrl + Space'
    paste_text_from_clipboard_shortcut: str = 'Ctrl + Shift + V'
    clear_document_shortcut: str = 'Ctrl + Shift + P'
    open_settings_shortcut: str = 'Ctrl + Shift + S'
    screenshot_shortcut: str = 'Shift + Windows + S'
    open_document_shortcut: str = 'Ctrl + O'


class DocumentSettingsSchema(BaseModel):
    doctype: str = 'docx'
    out_file: str = 'out.docx'
    create_new_file: bool = False


class StyleSettingsSchema(BaseModel):
    font: str = 'Times New Roman'
    font_size: int = 14


class TextSettingsSchema(BaseModel):
    caption: str = 'Рис.{number}'
    task_header: str = 'Завдання №{number}'


class InterfaceSettingsSchema(BaseModel):
    language: str = 'en'


class OthersSettingsSchema(BaseModel):
    temp_image_file: str = 'temp.png'


class SettingsSchema(BaseModel):
    text: TextSettingsSchema = TextSettingsSchema()
    others: OthersSettingsSchema = OthersSettingsSchema()
    style: StyleSettingsSchema = StyleSettingsSchema()
    document: DocumentSettingsSchema = DocumentSettingsSchema()
    shortcuts: ShortcutsSettingsSchema = ShortcutsSettingsSchema()
    interface: InterfaceSettingsSchema = InterfaceSettingsSchema()
