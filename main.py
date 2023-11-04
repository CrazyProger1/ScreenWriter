import loguru

from src.logging import setup_logging

setup_logging(loguru.logger)

from src.utils.keyboard import KeyboardManager

mgr = KeyboardManager()


def hello():
    print('Hello!')


def hello2():
    print('Hello2!')


mgr.register('Ctrl + O', hello)
mgr.register('Ctrl + O', hello2)
# mgr.unregister('Ctrl + O', hello)

while 1:
    pass
