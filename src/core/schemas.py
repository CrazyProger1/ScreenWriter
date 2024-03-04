from pydantic import BaseModel


class Shortcuts(BaseModel):
    exit: str = 'Ctrl + Shift + Q'
    open_document: str = 'Ctrl + Shift + O'
    start_current_document: str = 'Ctrl + Shift + D'
    new_document: str = 'Ctrl + Shift + N'
    clear_current_document: str = 'Ctrl + Shift + C'
    paste_clipboard_content: str = 'Ctrl + Shift + V'
    open_settings: str = 'Ctrl + Shift + S'
    reset_settings: str = 'Ctrl + Shift + R'
    add_task_header: str = 'Ctrl + Shift + Space'
    screenshot: str = 'Windows + Shift + S'


class Document(BaseModel):
    current_document: str = 'document.docx'
    autoclear_document: bool = False


class Style(BaseModel):
    font: str = 'Times New Roman'
    font_size: int = 14
    caption_format: str = 'Рис. {number}'
    task_header_format: str = 'Завдання №{number}'


class UI(BaseModel):
    language: str = 'en'


class Other(BaseModel):
    temporary_file: str = 'temp.png'


class Settings(BaseModel):
    shortcuts: Shortcuts = Shortcuts()
    document: Document = Document()
    style: Style = Style()
    ui: UI = UI()
    other: Other = Other()


class Arguments(BaseModel):
    settings_file: str = 'settings.toml'


class Context(BaseModel):
    task_counter: int = 0
    screenshot_counter: int = 0
