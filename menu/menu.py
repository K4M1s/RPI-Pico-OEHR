import math

from display.display import Display
from lcd.lcd import CursorMode
from menu.items.current_position import CurrentPosition
from menu.items.set_max import SetMAX
from menu.items.set_min import SetMIN
from menu.items.set_range_max import SetRangeMAX
from menu.items.set_range_min import SetRangeMIN


class Menu:
    def __init__(self, display: Display, config, state):
        self.items = [
            SetMIN(display, config),
            SetMAX(display, config),
            SetRangeMIN(display, config),
            SetRangeMAX(display, config),
            CurrentPosition(display, config, state)
        ]
        self.page = 0
        self.cursor = 0
        self.display = display
        self.items_count = len(self.items)
        self.items_per_page = self.display.lcd.num_rows
        self.pages = math.ceil(self.items_count / self.items_per_page)
        self.selected = None
        self.status = False

    def click(self):
        if not self.status:
            return

        if self.selected is None:
            self.selected = (self.page * self.items_per_page) - self.items_per_page + (self.cursor + 1) + 1
            print(self.selected)
        else:
            self.items[self.selected].click()
            self.selected = None

        self.display.lcd.clear()
        self.render()

    def hold(self):
        self.display.clear()
        self.status = not self.status
        if self.status:
            self.selected = None
            self.render()

    def up(self):
        if not self.status:
            return

        if self.selected is not None:
            self.items[self.selected].up()
            return

        if not self.items_count > (self.page * self.items_per_page) + self.cursor + 1:
            self.page = 0
        else:
            self.cursor += 1
            if self.cursor > self.items_per_page - 1:
                self.cursor = 0
                self.page += 1
                if self.page >= self.pages:
                    self.page = 0

        self.render()

    def down(self):
        if not self.status:
            return

        if self.selected is not None:
            self.items[self.selected].down()
            return

        self.cursor -= 1
        if self.cursor < 0:
            self.cursor = self.items_per_page - 1
            self.page -= 1
            if self.page < 0:
                self.page = self.pages - 1
                if (self.pages - 1) * self.items_per_page < self.items_count:
                    self.cursor = self.items_count - (self.pages - 1) * self.items_per_page - 1
        self.render()

    def render(self):
        if not self.status:
            return

        if self.selected is not None:
            self.items[self.selected].render()
            return

        for i in range(self.items_per_page):
            if self.items_count > (self.page * self.items_per_page) + i:
                self._render_line(i, self.items[(self.page * self.items_per_page) + i].title)
            else:
                self._render_line(i, '')

    def _render_line(self, row, text):

        if len(text) >= self.display.lcd.num_cols:
            text = text[0:self.display.lcd.num_cols - 1]

        text_length = len(text) + 1

        self.display.lcd.set_cursor_pos(row, 1)
        self.display.lcd.print(text)
        if text_length < self.display.lcd.num_cols:
            self.display.lcd.set_cursor_pos(row, text_length)
            to_clear = self.display.lcd.num_cols - text_length
            self.display.lcd.print(to_clear * ' ')
        self.display.lcd.set_cursor_pos(self.cursor, 0)
        self.display.lcd.set_cursor_mode(CursorMode.LINE)
