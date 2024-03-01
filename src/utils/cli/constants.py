import colorama

INFO_COLOR = colorama.Fore.LIGHTBLUE_EX
INFO_BG_COLOR = ''
INFO_PREFIX = '[*]'
POSITIVE_COLOR = colorama.Fore.GREEN
POSITIVE_BG_COLOR = ''
POSITIVE_PREFIX = '[+]'
NEGATIVE_COLOR = colorama.Fore.RED
NEGATIVE_BG_COLOR = ''
NEGATIVE_PREFIX = '[-]'

DEFAULT_STYLES = {
    'default': {
        'color': '',
        'bg_color': '',
        'prefix': ''
    },
    'info': {
        'color': INFO_COLOR,
        'bg_color': INFO_BG_COLOR,
        'prefix': INFO_PREFIX,
    },
    'positive': {
        'color': POSITIVE_COLOR,
        'bg_color': POSITIVE_BG_COLOR,
        'prefix': POSITIVE_PREFIX,
    },
    'negative': {
        'color': NEGATIVE_COLOR,
        'bg_color': NEGATIVE_BG_COLOR,
        'prefix': NEGATIVE_PREFIX,
    }
}
