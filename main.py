import argparse

from app import CLIApp


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    app = CLIApp(args)
    app.run()
