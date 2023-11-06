import loguru

from src.core import Core
from src.context import Context
from src.cli import CLI
from src.logging import setup_logging

if __name__ == '__main__':
    setup_logging(loguru.logger)
    context = Context()
    cli = CLI(context=context)
    core = Core(context=context)
    cli.run()
    core.run()

