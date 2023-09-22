from loguru import logger

from app.app import App
from app.cli.view import create_cli


class CLIApp(App):
    def run(self):
        logger.info('Running app...')
        cli = create_cli(settings=self.settings)
        cli.show()
        super(CLIApp, self).run()
        cli.destroy()
        logger.info('App terminated')
