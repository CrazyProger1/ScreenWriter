import colorama


def reset_styles():
    print(colorama.Style.RESET_ALL, sep='', end='')


def colorize(color: str = colorama.Fore.WHITE, bg_color: str = ''):
    print(color, bg_color, sep='', end='')
