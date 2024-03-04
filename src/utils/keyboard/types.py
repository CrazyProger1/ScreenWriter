from abc import ABC, abstractmethod
from typing import Callable


class BaseKeyboardManager(ABC):
    @abstractmethod
    def add_callback(self, shortcut: str, callback: Callable) -> None: ...

    @abstractmethod
    def remove_callback(self, shortcut: str, callback: Callable) -> None: ...

    @abstractmethod
    def remove_shortcut(self, shortcut: str) -> None: ...
