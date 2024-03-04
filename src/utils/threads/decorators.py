from functools import wraps
from threading import Thread
from typing import Callable


def thread(target: Callable = None, /, daemon: bool = True):
    def wrapper(*args, **kwargs):
        thr = Thread(
            target=target,
            args=args,
            kwargs=kwargs,
            daemon=daemon
        )

        thr.start()
        return thr

    def decorator(target: Callable):
        nonlocal target
        return wraps(target)(wrapper)

    if target:
        return wraps(target)(wrapper)
    else:
        return decorator
