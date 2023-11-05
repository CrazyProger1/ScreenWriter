from typing import Callable


class Event:
    def __init__(self, ):
        self._listeners = {}
        self._last_instance = None

    def __get__(self, instance, owner):
        self._last_instance = instance
        return self

    def add_listener(self, listener: Callable, pass_subject: bool = False):
        if not callable(listener):
            raise TypeError('listener must be callable')
        if listener not in self._listeners.keys():
            self._listeners.update({listener: pass_subject})

    def __call__(self, *args, **kwargs):
        for listener, pass_subj in self._listeners.items():
            if pass_subj:
                listener(self._last_instance, *args, **kwargs)
            else:
                listener(*args, **kwargs)
