from abc import ABC, abstractmethod
from typing import Literal, Iterable, Generator

type Mode = Literal[
    'w',
    'r',
    'a'
]


class Component(ABC):
    pass


class Style(ABC):
    pass


class Document(ABC):
    @abstractmethod
    def __init__(self, file: str, mode: Mode): ...

    @abstractmethod
    def read(self) -> Iterable[Component]: ...

    @abstractmethod
    def write(self, component: Component): ...

    @abstractmethod
    def stylize(self, style: Style): ...

    @abstractmethod
    def __enter__(self) -> "Document": ...

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb): ...

    @abstractmethod
    def __iter__(self) -> Generator[Component, None, None]: ...
