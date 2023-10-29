from pydantic import BaseModel
from typeguard import typechecked

from .enums import Format
from .loaders import (
    Loader,
    get_loader
)


@typechecked
def load(
        schema: type[BaseModel],
        file: str,
        fmt: Format | str | None = None,
        loader: type[Loader] | None = None
):
    if not loader:
        loader = get_loader(fmt=fmt, file=file)
    return loader.load(schema=schema, file=file)


@typechecked
def save(
        instance: BaseModel,
        file: str,
        fmt: Format | str | None = None,
        loader: type[Loader] | None = None
):
    if not loader:
        loader = get_loader(fmt=fmt, file=file)
    return loader.save(instance=instance, file=file)
