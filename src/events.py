from src.utils import observer


class CoreEventChannel:
    screenshot_event = observer.Event()
    exit_event = observer.Event()
    open_logfile_event = observer.Event()
    open_document_event = observer.Event()
    open_settings_event = observer.Event()
    clear_document_event = observer.Event()
    settings_reset_event = observer.Event()

    invalid_doctype_error_event = observer.Event()
    permission_denied_error_event = observer.Event()


class UIEventChannel:
    user_input = observer.Event()
