import argparse

from app import CLI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    app = CLI(args)
    app.run()
