from pydantic import BaseModel


class Shortcuts(BaseModel):
    exit: str = 'Ctrl + Shift + Q'
    open_document: str = 'Ctrl + Shift + O'
    start_current_document: str = 'Ctrl + Shift + D'
    new_document: str = 'Ctrl + Shift + N'
    clear_current_document: str = 'Ctrl + Shift + C'
    paste_clipboard_content: str = 'Ctrl + Shift + V'
    open_settings: str = 'Ctrl + Shift + S'
    clear_settings: str = 'Ctrl + Shift + R'
    add_task_header: str = 'Ctrl + Shift + Space'
    screenshot: str = 'Windows + Shift + S'


class State(BaseModel):
    current_document: str = 'document.docx'
    autoclear_document: bool = False


class Style(BaseModel):
    font: str = 'Times New Roman'
    font_size: int = 14
    caption_format: str = 'Рис. {number}'
    task_header_format: str = 'Завдання №{number}'


class Settings(BaseModel):
    shortcuts: Shortcuts = Shortcuts()
    state: State = State()
    style: Style = Style()
