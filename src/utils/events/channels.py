from typing import Iterable

from .types import (
    BaseEventChannel,
    BaseEvent
)


class EventChannel(BaseEventChannel):
    @classmethod
    def events(cls) -> Iterable[BaseEvent]:
        events = set()

        for name, value in cls.__dict__.items():
            if isinstance(value, BaseEvent):
                events.add(value)
        return events
