import os
from abc import ABC, abstractmethod
from typing import get_type_hints

import toml
from pydantic import BaseModel

from .exceptions import (
    SettingsDecodeError,
    SettingsEncodeError,
    SettingsSchemaError
)


class Settings(ABC, BaseModel):

    @classmethod
    @abstractmethod
    def load(cls, file: str) -> 'Settings': ...

    @abstractmethod
    def save(self, file: str) -> None: ...


class TOMLSettings(Settings):
    def __init__(self, **data):
        super(TOMLSettings, self).__init__(**data)

    def __validate_curr_values(self):
        cls = self.__class__
        annotations = get_type_hints(cls)
        for field, value in self.__dict__.items():
            typehint = annotations.get(field)
            if not isinstance(value, typehint):
                raise SettingsEncodeError(f'Field {field} has wrong type value, it should be {typehint.__name__}')

    @classmethod
    def __validate_field_types(cls):
        annotations = get_type_hints(cls)
        dumpable_types = set(toml.TomlEncoder().dump_funcs.keys())

        for field, typehint in annotations.items():
            if typehint not in dumpable_types:
                raise SettingsSchemaError(f'Field {field} has undumpable type')

    @classmethod
    def load(cls, file: str) -> 'TOMLSettings':
        cls.__validate_field_types()

        if not os.path.isfile(file):
            raise FileNotFoundError(f'File {file} not found')
        try:
            data = toml.load(file)
        except toml.TomlDecodeError:
            raise SettingsDecodeError(f'File {file} has incorrect format, it should be toml')

        return cls.model_validate(data)

    def save(self, file: str) -> None:
        self.__validate_curr_values()

        try:
            data = self.model_dump()
        except TypeError:
            raise SettingsEncodeError('Encode error')

        with open(file, 'w', encoding='utf-8') as f:
            toml.dump(data, f)
