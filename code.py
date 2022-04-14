import board
import busio

from config.config import Config
from display.display import Display
from encoder.encoder import Encoder
from menu.menu import Menu
from state.State import State

i2c = busio.I2C(board.GP1, board.GP0, frequency=400000)
display = Display(i2c, 2, 16)
config = Config()
state = State(config)
menu = Menu(display, config, state)

encoder = Encoder(on_decrement=menu.down, on_increment=menu.up, on_button_click=menu.click, on_button_hold=menu.hold)

display.lcd.clear()

while True:
    state.update()
    encoder.tick()

    if not menu.status:
        display.display(int(state.position))
