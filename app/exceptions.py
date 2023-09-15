from dataclasses import dataclass
from typing import Callable


@dataclass
class ScreenWriterError(Exception):
    message: str


class DocumentSavingError(ScreenWriterError):
    pass


class SetupError(ScreenWriterError):
    pass


class ClipboardEmptyError(ScreenWriterError):
    pass


@dataclass
class KeyboardError(Exception):
    message: str


def catch_error(error_type: type[Exception], handler: Callable = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except error_type as e:
                if handler:
                    handler(e)

        return wrapper

    return decorator
