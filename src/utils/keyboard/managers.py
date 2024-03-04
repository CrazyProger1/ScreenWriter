from typing import Callable

import keyboard

from .types import BaseKeyboardManager


class KeyboardManager(BaseKeyboardManager):

    def __init__(self):
        self._shortcut_callbacks = {}

    def _handle_pressed(self, shortcut: str):
        for callback in self._shortcut_callbacks.get(shortcut, []):
            callback()

    def _add_hotkey(self, shortcut: str):
        keyboard.add_hotkey(shortcut, lambda: self._handle_pressed(shortcut))

    def add_callback(self, shortcut: str, callback: Callable) -> None:
        if shortcut not in self._shortcut_callbacks:
            self._add_hotkey(shortcut)

        callbacks = self._shortcut_callbacks.get(shortcut, [])
        callbacks.append(callback)
        self._shortcut_callbacks[shortcut] = callbacks

    def remove_callback(self, shortcut: str, callback: Callable) -> None:
        callbacks = self._shortcut_callbacks.get(shortcut, [])

        if callback in callbacks:
            callbacks.remove(callback)

    def remove_shortcut(self, shortcut: str) -> None:
        self._shortcut_callbacks.pop(shortcut, None)

    def __del__(self):
        for shortcut in self._shortcut_callbacks.keys():
            keyboard.remove_hotkey(shortcut)
