from abc import ABC, abstractmethod
from typing import Iterable, Callable


class BaseEvent(ABC):
    @abstractmethod
    def __init__(self, name: str): ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def channel(self) -> 'BaseEventChannel': ...

    @abstractmethod
    def subscribe(self, callback: Callable): ...

    @abstractmethod
    def publish(self, *args, **kwargs): ...

    @abstractmethod
    def __call__(self, *args, **kwargs): ...


class BaseAsyncEvent(BaseEvent, ABC):
    @abstractmethod
    async def publish(self, *args, **kwargs): ...

    @abstractmethod
    async def __call__(self, *args, **kwargs): ...


class BaseEventChannel(ABC):

    @classmethod
    @property
    @abstractmethod
    def events(cls) -> Iterable[BaseEvent]: ...
