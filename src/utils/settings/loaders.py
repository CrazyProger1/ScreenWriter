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
        if not os.path.isfile(file):
            raise FileNotFoundError(f'File {file} not found')

        try:
            data = toml.load(file)
        except toml.TomlDecodeError:
            raise

        return schema.model_validate(data)

    @classmethod
    @typechecked
    def save(cls, instance: BaseModel, file: str):
        pass


@cache
def get_loader(fmt: Format, file: str, raise_exception: bool = False) -> type[Loader] | None:
    ext = os.path.splitext(file)[1]
    for loader in Loader.__subclasses__():
        if not fmt:
            if isinstance(loader.filetypes, set) and ext in loader.filetypes:
                return loader
        else:
            if loader.format == fmt:
                return loader

    if raise_exception:
        raise ValueError(
            f"Loader can't be detected for file {file} with format {fmt}, "
            f"try specifying valid format or loader directly"
        )
