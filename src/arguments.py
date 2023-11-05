import argparse

from config import (
    APP,
    DESCRIPTION,
    DEFAULT_SETTINGS_FILE
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=APP,
        description=DESCRIPTION
    )

    parser.add_argument(
        '-s',
        '--settings',
        default=DEFAULT_SETTINGS_FILE,
        help='toml settings filepath'
    )

    parser.add_argument(
        'file',
        nargs='*',
        default=None,
        help='document filepath'
    )

    return parser.parse_args()
