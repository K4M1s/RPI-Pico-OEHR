import time

import board
import rotaryio
from digitalio import DigitalInOut, Pull


class Encoder:
    def __init__(self, on_decrement, on_increment, on_button_click, on_button_hold):
        self.button = DigitalInOut(board.GP16)
        self.button.pull = Pull.UP
        self.encoder = rotaryio.IncrementalEncoder(board.GP14, board.GP15)
        self.last_position = 0
        self.button_push_time = 0
        self.button_push_last_time = 0
        self.button_last_state = False
        self.decrement_callback = on_decrement
        self.increment_callback = on_increment
        self.button_click_callback = on_button_click
        self.button_hold_callback = on_button_hold
        self.counter = 0

    def tick(self):
        position = self.encoder.position
        if position != self.last_position:
            if position > self.last_position:
                self.increment_callback()
            else:
                self.decrement_callback()
        self.last_position = position

        self.counter += 1

        if not self.button.value:
            self.button_push_time += time.monotonic() - self.button_push_last_time
        else:
            if self.button.value != self.button_last_state:
                self.button_last_state = self.button.value
                if self.button_push_time > 0.4:
                    self.button_hold_callback()
                else:
                    self.button_click_callback()

            self.button_push_time = 0

        self.button_last_state = self.button.value
        self.button_push_last_time = time.monotonic()
