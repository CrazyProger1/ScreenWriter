import argparse

from config import APP, DESCRIPTION


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=APP,
        description=DESCRIPTION
    )

    parser.add_argument(
        'file',
        nargs='?',
        default=None,
        help='document filepath'
    )

    return parser.parse_args()
