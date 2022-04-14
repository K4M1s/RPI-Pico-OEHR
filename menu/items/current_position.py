from menu.menu_item import MenuItem
from state.State import State


class CurrentPosition(MenuItem):

    def __init__(self, display, config, state: State):
        super().__init__(display, config, "Akt. pozycja")
        self.state = state

    def render(self):
        self.display.lcd.set_cursor_pos(0, 0)
        self.display.lcd.print(self.title)
        self.display.lcd.set_cursor_pos(1, 0)
        self.display.lcd.print('    ')
        self.display.lcd.set_cursor_pos(1, 0)
        self.display.lcd.print(str(self.state.position_raw))
