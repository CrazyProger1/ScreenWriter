import colorama

from .prints import (
    print_colored,
    print_info,
    print_positive,
    print_negative
)

colorama.init()

__all__ = [
    'print_colored',
    'print_info',
    'print_positive',
    'print_negative',
]
