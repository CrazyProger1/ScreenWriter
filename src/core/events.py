from src.utils.events import (
    EventChannel,
    Event
)


class MainChannel(EventChannel):
    screenshot_taken = Event()
    document_opened = Event()
    document_started = Event()
    new_document_created = Event()
    document_cleared = Event()
    content_pasted = Event()
    settings_opened = Event()
    settings_reset = Event()
    task_header_added = Event()
    terminated = Event()
