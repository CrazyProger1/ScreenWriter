import pyperclip


def clear():
    pyperclip.copy('')


def write(text: str):
    return pyperclip.copy(text)


def read() -> str:
    return pyperclip.paste()
