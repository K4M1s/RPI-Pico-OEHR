bar = {
    1: bytearray([
        0b11100,
        0b11110,
        0b11110,
        0b11110,
        0b11110,
        0b11110,
        0b11110,
        0b11100
    ]),
    2: bytearray([
        0b00111,
        0b01111,
        0b01111,
        0b01111,
        0b01111,
        0b01111,
        0b01111,
        0b00111
    ]),
    3: bytearray([
        0b11111,
        0b11111,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11111,
        0b11111
    ]),
    4: bytearray([
        0b11110,
        0b11100,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11000,
        0b11100
    ]),
    5: bytearray([
        0b01111,
        0b00111,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00011,
        0b00111
    ]),
    6: bytearray([
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b11111,
        0b11111
    ]),
    7: bytearray([
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00111,
        0b01111
    ]),
    8: bytearray([
        0b11111,
        0b11111,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000,
        0b00000
    ])
}


def register_characters(lcd):
    for i in range(0, 8):
        lcd.create_char(i, bar[i+1])
    pass


def custom0(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(7)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(1)
    lcd.write(5)
    lcd.write(0)


def custom1(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(32)
    lcd.write(32)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(32)
    lcd.write(32)
    lcd.write(0)


def custom2(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(4)
    lcd.write(2)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(1)
    lcd.write(5)
    lcd.write(5)


def custom3(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(4)
    lcd.write(2)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(6)
    lcd.write(5)
    lcd.write(0)


def custom4(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(5)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(32)
    lcd.write(32)
    lcd.write(0)


def custom5(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(2)
    lcd.write(3)
    lcd.set_cursor_pos(1, col)
    lcd.write(6)
    lcd.write(5)
    lcd.write(0)


def custom6(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(2)
    lcd.write(3)
    lcd.set_cursor_pos(1, col)
    lcd.write(1)
    lcd.write(5)
    lcd.write(0)


def custom7(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(7)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(32)
    lcd.write(32)
    lcd.write(0)


def custom8(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(2)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(1)
    lcd.write(5)
    lcd.write(0)


def custom9(lcd, col):
    lcd.set_cursor_pos(0, col)
    lcd.write(1)
    lcd.write(2)
    lcd.write(0)
    lcd.set_cursor_pos(1, col)
    lcd.write(6)
    lcd.write(5)
    lcd.write(0)


def print_number(lcd, value, col):
    if value == 0:
        custom0(lcd, col)
    elif value == 1:
        custom1(lcd, col)
    elif value == 2:
        custom2(lcd, col)
    elif value == 3:
        custom3(lcd, col)
    elif value == 4:
        custom4(lcd, col)
    elif value == 5:
        custom5(lcd, col)
    elif value == 6:
        custom6(lcd, col)
    elif value == 7:
        custom7(lcd, col)
    elif value == 8:
        custom8(lcd, col)
    elif value == 9:
        custom9(lcd, col)
