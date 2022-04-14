from analogio import AnalogIn
import board

from config.config import Config


def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    val = ((val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

    if val < dst[0]:
        return dst[0]

    if val > dst[1]:
        return dst[1]

    return val



class State:

    def __init__(self, config: Config):
        self.config = config
        self.pin = AnalogIn(board.A0)
        self.position_raw = 0
        self.position = 0
        self.update()

    def calculate(self):
        self.position = scale(self.position_raw, (self.config.range_min, self.config.range_max), (0, 100))

    def update(self):
        self.position_raw = self.pin.value
        self.calculate()
