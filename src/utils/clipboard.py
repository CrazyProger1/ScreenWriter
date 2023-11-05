from time import sleep

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
    except Exception as e:
        pass
