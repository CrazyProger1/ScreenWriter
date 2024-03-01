import logging

from pydantic import BaseModel

from src.utils.arguments import SchemedArgumentParser
from src.utils.settings import (
    load,
    save,
    TOMLLoader,
    BaseLoader
)


def parse_arguments(schema: type[BaseModel]) -> BaseModel:
    parser = SchemedArgumentParser(
        schema=schema,
    )

    return parser.parse_schemed_args()


def save_settings(file: str, settings: BaseModel, loader: BaseLoader = TOMLLoader(), default_file: str = None) -> None:
    try:
        save(
            file=file,
            instance=settings,
            loader=loader
        )
    except OSError:
        if default_file:
            return save_settings(
                file=default_file,
                settings=settings,
                loader=loader
            )
        raise


def load_settings(
        file: str,
        schema: type[BaseModel],
        loader: BaseLoader = TOMLLoader(),
        default_file: str = None
) -> BaseModel:
    try:
        return load(
            file=file,
            schema=schema,
            loader=loader
        )
    except (FileNotFoundError, OSError):
        settings = schema()
        save_settings(
            file=file,
            settings=settings,
            loader=loader,
            default_file=default_file
        )
        return settings


def decorate_logger(logger: logging.Logger, logging_format: str):
    try:
        import colorlog

        formatter = colorlog.ColoredFormatter(
            logging_format,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
    except ImportError:
        pass
