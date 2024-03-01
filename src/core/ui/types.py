from abc import ABC, abstractmethod
from enum import Enum

from pydantic import BaseModel


class BaseUI(ABC):
    mode: str | Enum

    @abstractmethod
    def __init__(self, arguments: BaseModel, settings: BaseModel, context: BaseModel): ...

    @abstractmethod
    def run(self): ...


class BaseUIFactory(ABC):
    @classmethod
    @abstractmethod
    def create(cls, mode: str | Enum, arguments: BaseModel, settings: BaseModel, context: BaseModel) -> BaseUI: ...
