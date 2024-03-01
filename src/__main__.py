import logging

from src.core.config import (
    DEFAULT_SETTINGS_FILE,
    APP,
    LOGGING_LEVEL,
    LOGGING_FORMAT
)
from src.core.schemas import (
    Arguments,
    Settings
)
from src.core.utils import (
    parse_arguments,
    load_settings,
    decorate_logger
)


def main():
    logger = logging.getLogger(APP)
    logger.setLevel(LOGGING_LEVEL)
    decorate_logger(
        logger=logger,
        logging_format=LOGGING_FORMAT
    )
    logger.info(f'Application launched')

    args = parse_arguments(schema=Arguments)
    logger.info(f'Arguments parsed: {args}')

    settings = load_settings(
        file=args.settings_file,
        schema=Settings,
        default_file=DEFAULT_SETTINGS_FILE
    )
    logger.info(f'Settings parsed: {settings}')

    logger.info(f'Application terminated')


if __name__ == '__main__':
    main()
