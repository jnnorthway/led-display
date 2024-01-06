import math
import common
from rpi_ws281x import Adafruit_NeoPixel, Color

WIDTH = 32
HEIGHT = 8
CONFIG = common.load_config()
STRIP = Adafruit_NeoPixel(
    CONFIG["led"]["count"],
    CONFIG["led"]["pin"],
    CONFIG["led"]["frequency"],
    CONFIG["led"]["dma"],
    CONFIG["led"]["inverted"],
    CONFIG["led"]["brightness"],
    CONFIG["led"]["channel"],
)
STRIP.begin()

COLOR_TRANSLATION = {
    "white": Color(255, 255, 255),
    "black": Color(0, 0, 0),
    "red": Color(255, 0, 0),
}


def pack_subs(logo, number_array):
    current_number = 0
    current_pixel = 0
    logo_width = len(logo[0])
    for i in range(0, WIDTH):
        x = int(i)
        for j in range(0, HEIGHT):
            y = int(j)
            if x < logo_width:
                colour = COLOR_TRANSLATION[logo[y][x]]
            else:
                colour = COLOR_TRANSLATION[
                    number_array[current_number][y][current_pixel]
                ]
            z = x * j
            col = math.floor(z / HEIGHT)
            if col % 2 == 0:
                px = z % HEIGHT
            else:
                px = HEIGHT - ((z + 1) % HEIGHT)
            STRIP.setPixelColor(px, colour)
        if x >= logo_width:
            current_pixel += 1
            if current_pixel == len(number_array[current_number][y]):
                current_number += 1
                current_pixel = 0
    STRIP.show()
