import inspect
from typing import Callable

from typeguard import typechecked

from .types import (
    BaseEvent,
    BaseAsyncEvent,
    BaseEventChannel
)


class Event(BaseEvent):
    @typechecked
    def __init__(self, name: str | None = None):
        self._name = name
        self._callbacks = []
        self._channel = None

    def __set_name__(self, owner, name):
        self._channel = owner
        self._name = name

    @property
    def channel(self) -> BaseEventChannel:
        return self._channel

    @property
    def name(self) -> str:
        return self._name

    @typechecked
    def subscribe(self, callback: Callable):
        self._callbacks.append(callback)

    def publish(self, *args, **kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.publish(*args, **kwargs)


class AsyncEvent(BaseAsyncEvent, Event):

    async def publish(self, *args, **kwargs):
        for callback in self._callbacks:
            if inspect.iscoroutinefunction(callback):
                await callback(*args, **kwargs)
            else:
                callback(*args, **kwargs)

    async def __call__(self, *args, **kwargs):
        await self.publish(*args, **kwargs)
