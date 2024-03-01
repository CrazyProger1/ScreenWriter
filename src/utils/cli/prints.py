import colorama

from .utils import (
    colorize,
    reset_styles
)
from .styles import get_style


def print_colored(
        *values,
        sep: str = ' ',
        end: str = '\n',
        color: str = colorama.Fore.WHITE,
        bg_color: str = ''):
    colorize(color=color, bg_color=bg_color)
    print(*values, sep=sep, end=end)
    reset_styles()


def print_info(*values, **kwargs):
    style = get_style('info')
    kwargs.update(style)

    print_colored(
        kwargs.pop('prefix'),
        *values,
        **kwargs
    )


def print_positive(*values, **kwargs):
    style = get_style('positive')
    kwargs.update(style)

    print_colored(
        kwargs.pop('prefix'),
        *values,
        **kwargs
    )


def print_negative(*values, **kwargs):
    style = get_style('negative')
    kwargs.update(style)

    print_colored(
        kwargs.pop('prefix'),
        *values,
        **kwargs
    )
