import toml
from pydantic import BaseModel
from typeguard import typechecked

from .types import BaseLoader
from .exceptions import (
    FileFormatError
)


class TOMLLoader(BaseLoader):
    filetypes = {
        '.toml',
    }

    @typechecked
    def load(self, file: str, schema: type[BaseModel], **kwargs) -> BaseModel:
        try:
            data: dict = toml.load(file)
            return schema.model_validate(data, **kwargs)
        except toml.TomlDecodeError as e:
            raise FileFormatError(file=file, msg=str(e))

    @typechecked
    def save(self, file: str, instance: BaseModel, **kwargs) -> None:
        with open(file, 'w', encoding='utf-8') as f:
            data: dict = instance.model_dump(**kwargs)
            toml.dump(data, f)
