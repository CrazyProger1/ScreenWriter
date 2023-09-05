from time import sleep

import pyperclip
from PIL import ImageGrab


def save_screenshot(file: str):
    img = ImageGrab.grabclipboard()
    while not img:
        try:
            img = ImageGrab.grabclipboard()
            sleep(0.1)
        except OSError:
            pass
    try:
        img.save(file)
    except:
        pass


def clear():
    pyperclip.copy('')


def write(text: str):
    return pyperclip.copy(text)


def read() -> str:
    return pyperclip.paste()
