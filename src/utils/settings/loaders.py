import os.path
from abc import ABC, abstractmethod
from functools import cache

import toml
from pydantic import BaseModel
from typeguard import typechecked

from .enums import Format


class Loader(ABC):
    format: Format | str = None
    filetypes: set[str] = None

    @classmethod
    @abstractmethod
    def load(cls, schema: type[BaseModel], file: str) -> BaseModel: ...

    @classmethod
    @abstractmethod
    def save(cls, instance: BaseModel, file: str): ...


class TOMLLoader(Loader):
    format = Format.TOML
    filetypes = {
        '.toml',
    }

    @classmethod
    @typechecked
    def load(cls, schema: type[BaseModel], file: str) -> BaseModel:
        data = toml.load(file)
        print(data)

    @classmethod
    @typechecked
    def save(cls, instance: BaseModel, file: str):
        pass


@cache
def get_loader(fmt: Format, file: str) -> type[Loader] | None:
    ext = os.path.splitext(file)[1]
    for loader in Loader.__subclasses__():
        if not fmt:
            if isinstance(loader.filetypes, set) and ext in loader.filetypes:
                return loader
        else:
            if loader.format == fmt:
                return loader
