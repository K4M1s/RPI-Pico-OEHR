import lcd.lcd
from display.numbers import register_characters, print_number
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import LCD


class Display:

    def __init__(self, i2c, rows, cols):
        self.lcd = LCD(I2CPCF8574Interface(i2c, 0x20), num_rows=rows, num_cols=cols)
        register_characters(self.lcd)
        self.currently_displaying = -1

    def clear(self):
        self.lcd.clear()
        self.currently_displaying = -1

    def display(self, n):
        if n == self.currently_displaying:
            return

        if n < 10 and self.currently_displaying > 9:
            self.clear()

        if n < 100 and self.currently_displaying > 99:
            self.clear()

        self.lcd.set_cursor_mode(lcd.lcd.CursorMode.HIDE)
        self.currently_displaying = n

        number = n
        d = 0
        c = 0
        u = 0

        if number > 99:
            c = (number - (number % 100)) / 100
            number = number % 100
        else:
            c = 0

        if number > 9:
            d = (number - (number % 10)) / 10
            number = number % 10
        else:
            d = 0

        u = number

        offset = 3
        if n >= 100:
            print_number(self.lcd, c, offset)
        else:
            offset = 2

        if n >= 10:
            print_number(self.lcd, d, offset+3)
        else:
            offset = 0

        print_number(self.lcd, u, offset+6)
