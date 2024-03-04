from time import sleep

from PIL import ImageGrab


def save_image(file: str):
    image = ImageGrab.grabclipboard()
    while not image:
        try:
            image = ImageGrab.grabclipboard()
            sleep(0.1)
        except OSError:
            pass
    try:
        image.save(file)
    except:
        pass
