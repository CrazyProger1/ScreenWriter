from dataclasses import dataclass

from src.core.types import (
    BaseComponent
)


@dataclass
class Image(BaseComponent):
    path: str
    caption: str


@dataclass
class Text(BaseComponent):
    text: str


@dataclass
class Header(BaseComponent):
    text: str
