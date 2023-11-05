import loguru

from src.logging import setup_logging

from src.l18n import _, ErrorMessages

print(_(ErrorMessages.ABC))

setup_logging(loguru.logger)

from src.arguments import parse_arguments

print(parse_arguments())
