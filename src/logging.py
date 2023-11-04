from config import (
    LOGGING_VERBOSITY,
    LOGGING_LEVEL,
    LOG_FILE
)


def setup_logging(logger):
    if not LOGGING_VERBOSITY:
        logger.remove()

    logger.add(
        LOG_FILE,
        level=LOGGING_LEVEL,
        rotation='100 KB',
        compression='zip'
    )
