from abc import ABC, abstractmethod


class BaseComponent(ABC):
    pass


class BaseStyle(ABC):
    pass


class BaseDocumentManager(ABC):
    @abstractmethod
    def open_document(self, file: str): ...

    @abstractmethod
    def clear_document(self): ...

    @abstractmethod
    def add_component(self, component: BaseComponent): ...

    @abstractmethod
    def stylize(self, style: BaseStyle): ...

    @property
    @abstractmethod
    def content(self) -> str: ...
