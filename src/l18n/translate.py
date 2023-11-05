import functools
import gettext
from enum import Enum

from config import LOCALEDIR, DEFAULT_LANGUAGE
from typeguard import typechecked


@typechecked
def set_language(language: str):
    global _translate
    translation = gettext.translation(
        domain='app',
        localedir=LOCALEDIR,
        languages=[language]
    )
    _translate = translation.gettext
    return translation.gettext


_translate = set_language(DEFAULT_LANGUAGE)


@functools.cache
@typechecked
def _(key: Enum | str) -> str:
    if isinstance(key, Enum):
        key = key.value

    return _translate(key)
