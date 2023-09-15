from typing import Iterable, Callable

import colorama

colorama.init()

styles = {
    'positive': colorama.Fore.GREEN,
    'negative': colorama.Fore.RED,
    'question': colorama.Fore.YELLOW,
    'status': colorama.Fore.BLUE,
    'info': colorama.Fore.LIGHTYELLOW_EX,
    'raw': colorama.Fore.WHITE
}


def reset_styles():
    """Resets console output style"""

    print(colorama.Style.RESET_ALL, sep='', end='')


def colorize(color=colorama.Fore.WHITE, bg_color=''):
    """Colorizes console output"""

    print(color, bg_color, sep='', end='')


def print_colored(*values, sep=' ', end='\n', color=colorama.Fore.WHITE, bg_color=''):
    """Prints colored output"""

    colorize(color=color, bg_color=bg_color)
    print(*values, sep=sep, end=end)
    reset_styles()


def print_prefixed(prefix, *values, sep=' ', end='\n'):
    """Prints prefix and values. Needed for print_pos, print_neg, ..."""

    print(f'{prefix} ', sep='', end='')
    print(*values, sep=sep, end=end)


def print_pos(*values, sep=' ', end='\n'):
    """Prints positive info with prefix [+]"""

    colorize(color=styles['positive'])
    print_prefixed('[+]', *values, sep=sep, end=end)
    reset_styles()


def print_neg(*values, sep=' ', end='\n'):
    """Prints negative info with prefix [-]"""

    colorize(color=styles['negative'])
    print_prefixed('[-]', *values, sep=sep, end=end)
    reset_styles()


def print_status(*values, sep=' ', end='\n'):
    colorize(color=styles['status'])
    print_prefixed('[~]', *values, sep=sep, end=end)
    reset_styles()


def print_info(*values, sep=' ', end='\n'):
    colorize(color=styles['info'])
    print_prefixed('[*]', *values, sep=sep, end=end)
    reset_styles()


def print_raw(*values, sep=' ', end='\n'):
    colorize(color=styles['raw'])
    print(*values, sep=sep, end=end)
    reset_styles()


def print_question(*values, sep=' ', end='\n'):
    """Prints question with prefix [?]"""

    colorize(color=styles['question'])
    print_prefixed('[?]', *values, sep=sep, end=end)
    reset_styles()


class ValidationError(ValueError):
    pass


def ask(
        prompt: str,
        default: any = None,
) -> str:
    print_question(prompt)
    value = input('[>] ')

    return value or default


def ask_validated(
        prompt: str,
        validator: Callable[[str], bool | None],
        default: any = None,
        exception: Exception = ValidationError
):
    value = ask(
        prompt=prompt,
        default=default
    )
    try:
        if not validator(value):
            raise ValidationError
        return value
    except exception as e:
        print_neg(str(e) or 'Value is invalid')
        return ask_validated(
            prompt=prompt,
            validator=validator,
            default=default
        )


def ask_bool(prompt: str, default: bool = False):
    value = ask(
        prompt=prompt,
        default=default
    )

    return value and str(value).lower() in {'1', 'y', 'yes', 'true', 't', True}


def ask_option(
        prompt: str,
        options: Iterable,
        default: any = None
) -> str:
    if not isinstance(options, Iterable):
        raise TypeError('options must be iterable')

    option_tuple = tuple(options)

    print_question(prompt)

    for i, option in enumerate(option_tuple):
        print(f'[{i}]', option)

    value = input('[>] ')

    if not value:
        return default

    if value.isdigit():
        index = abs(int(value))
        if len(option_tuple) > index:
            return option_tuple[index]

    elif value in option_tuple:
        return value

    return default


def setup_styles(**stls):
    styles.update(stls)
