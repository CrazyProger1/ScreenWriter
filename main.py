import loguru

from src.logging import setup_logging

setup_logging(loguru.logger)

from src.cli.l18n import _, ErrorMessages

print(_(ErrorMessages.ABC))
