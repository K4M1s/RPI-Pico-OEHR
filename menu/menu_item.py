from config.config import Config
from display.display import Display


class MenuItem:
    def __init__(self, display: Display, config: Config, title):
        self.display = display
        self.config = config
        self.title = title

    def up(self):
        pass

    def down(self):
        pass

    def click(self):
        pass

    def render(self):
        pass
