import argparse

from loguru import logger

from app import CLIApp
from config import (
    LOGGING_VERBOSITY,
    LOGGING_LEVEL,
    LOG_FILE
)


def setup_logging():
    if not LOGGING_VERBOSITY:
        logger.remove()

    logger.add(
        LOG_FILE,
        level=LOGGING_LEVEL,
        rotation='100 KB',
        compression='zip'
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    setup_logging()
    app = CLIApp(args)
    app.run()
