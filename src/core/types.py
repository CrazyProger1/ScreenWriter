from abc import ABC, abstractmethod


class BaseComponent(ABC):
    pass


class BaseDocumentManager(ABC):
    @abstractmethod
    def open_document(self, file: str): ...

    @abstractmethod
    def clear_document(self): ...

    @property
    @abstractmethod
    def content(self) -> str: ...

    @abstractmethod
    def add_component(self, component: BaseComponent): ...
