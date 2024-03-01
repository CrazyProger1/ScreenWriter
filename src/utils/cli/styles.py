from typeguard import typechecked

from .constants import (
    DEFAULT_STYLES
)
from .types import (
    STYLE
)

global_styles = DEFAULT_STYLES.copy()


@typechecked
def get_style(key: str) -> STYLE:
    return global_styles.get(key, global_styles['default'])


@typechecked
def stylize(key: str, style: STYLE):
    global_styles[key] = style
