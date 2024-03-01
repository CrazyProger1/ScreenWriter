import logging

from src.core.config import (
    DEFAULT_SETTINGS_FILE,
    APP,
    LOGGING_LEVEL,
    LOGGING_FORMAT,
    DEBUG
)

from src.core.schemas import (
    Arguments,
    Settings,
    Context
)
from src.core.utils import (
    parse_arguments,
    load_settings,
    decorate_logger
)
from src.core.ui import (
    UIFactory,
    GraphicMode
)
from src.core.core import Core


def main():
    logger = logging.getLogger(APP)
    logger.setLevel(LOGGING_LEVEL)

    if DEBUG:
        decorate_logger(
            logger=logger,
            logging_format=LOGGING_FORMAT
        )
    logger.info(f'Application launched')

    arguments = parse_arguments(schema=Arguments)
    logger.info(f'Arguments parsed: {arguments}')

    settings = load_settings(
        file=arguments.settings_file,
        schema=Settings,
        default_file=DEFAULT_SETTINGS_FILE
    )
    logger.info(f'Settings parsed: {settings}')

    context = Context()
    logger.info(f'Context created: {context}')

    ui = UIFactory.create(
        mode=GraphicMode.CLI,
        arguments=arguments,
        settings=settings,
        context=context
    )
    core = Core(
        arguments=arguments,
        settings=settings,
        context=context
    )

    ui.run()
    core.run()

    logger.info(f'Application terminated')


if __name__ == '__main__':
    main()
