from menu.menu_item import MenuItem


class SetMAX(MenuItem):

    def __init__(self, display, config):
        super().__init__(display, config, "Ustaw MAX")
        self.value = config.max

    def click(self):
        self.config.max = self.value
        self.config.write()

    def up(self):
        if self.value < 100:
            self.value += 2
        self.render()

    def down(self):
        if self.value > 0:
            self.value -= 2
        self.render()

    def render(self):
        self.display.lcd.set_cursor_pos(0, 0)
        self.display.lcd.print(self.title)
        self.display.lcd.set_cursor_pos(1, 0)
        self.display.lcd.print('   ')
        self.display.lcd.set_cursor_pos(1, 0)
        self.display.lcd.print(str(self.value))
