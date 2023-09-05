from app.app import App
from app.cli.menus import BaseCLI


class CLIApp(App):
    def run(self):
        cli = BaseCLI(self.settings)
        cli.show()
        super(CLIApp, self).run()
        cli.destroy()
