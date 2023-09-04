from app.app import App


class CLI(App):
    def run(self):
        print(self.settings)
