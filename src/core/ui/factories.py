from enum import Enum

from pydantic import BaseModel
from typeguard import typechecked

from .types import (
    BaseUIFactory,
    BaseUI
)
from src.utils.clsutils import iter_subclasses


class UIFactory(BaseUIFactory):
    @classmethod
    @typechecked
    def create(cls, mode: str | Enum, arguments: BaseModel, settings: BaseModel, context: BaseModel) -> BaseUI:
        for subclass in iter_subclasses(BaseUI):
            if subclass.mode == mode:
                return subclass(
                    arguments=arguments,
                    settings=settings,
                    context=context
                )
        raise ValueError(f'No such UI with mode: {mode}')
