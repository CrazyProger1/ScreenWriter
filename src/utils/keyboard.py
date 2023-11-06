from typing import Callable

import keyboard
from typeguard import typechecked
from loguru import logger


class ShortcutManager:
    def __init__(self):
        self._callbacks = {}

    def _call(self, shortcut: str):
        for callback in self._callbacks[shortcut]:
            callback()

    def _register_new_shortcut(self, shortcut: str):
        keyboard.add_hotkey(shortcut, self._call, args=(shortcut,))
        logger.info(f'Shortcut {shortcut} registered')

    @typechecked
    def register(self, shortcut: str, callback: Callable):
        if shortcut in self._callbacks:
            self._callbacks[shortcut].append(callback)
        else:
            self._callbacks[shortcut] = [callback]
            self._register_new_shortcut(shortcut)

        logger.debug(f'Callback {callback} for shortcut {shortcut} registered')

    @typechecked
    def unregister(self, shortcut: str, callback: Callable):
        if shortcut in self._callbacks:
            try:
                self._callbacks[shortcut].remove(callback)
                logger.debug(f'Callback {callback} for shortcut {shortcut} unregistered')
            except ValueError:
                pass
