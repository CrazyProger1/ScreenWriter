from app.app import App
from app.cli.view import create_cli


class CLIApp(App):
    def run(self):
        cli = create_cli(settings=self.settings)
        cli.show()
        super(CLIApp, self).run()
        cli.destroy()
