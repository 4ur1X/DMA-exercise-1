# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board
from rainbowio import colorwheel

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 1

while True:
    #india flag
    led[0] = (255,69,0)
    time.sleep(1)
    led[0] = (0,0,255)
    time.sleep(1)
    led[0] = (0, 128, 0)
    time.sleep(1)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #uae flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0, 128, 0)
    time.sleep(1)
    led[0] = (255,255,255)
    time.sleep(1)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #australia flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0,0,255)
    time.sleep(1)
    led[0] = (255,255,255)
    time.sleep(1)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #singapore flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (255,255,255)
    time.sleep(1)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #united states flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0,0,255)
    time.sleep(1)
    led[0] = (255,255,255)
    time.sleep(1)

    led[0] = (0, 0, 0)
    time.sleep(3)

    #-----------------------

    #india flag
    led[0] = (255,69,0)
    time.sleep(1)
    led[0] = (0,0,255)
    time.sleep(0.25)
    led[0] = (0, 128, 0)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(0.25)

    #uae flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0, 128, 0)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #australia flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0,0,255)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #singapore flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #united states flag
    led[0] = (255, 0, 0)
    time.sleep(1)
    led[0] = (0,0,255)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(3)

    #-------------------

    #india flag
    led[0] = (255,69,0)
    time.sleep(0.25)
    led[0] = (0,0,255)
    time.sleep(0.25)
    led[0] = (0, 128, 0)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #uae flag
    led[0] = (255, 0, 0)
    time.sleep(0.25)
    led[0] = (0, 128, 0)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #australia flag
    led[0] = (255, 0, 0)
    time.sleep(0.25)
    led[0] = (0,0,255)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #singapore flag
    led[0] = (255, 0, 0)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(1)

    #united states flag
    led[0] = (255, 0, 0)
    time.sleep(0.25)
    led[0] = (0,0,255)
    time.sleep(0.25)
    led[0] = (255,255,255)
    time.sleep(0.25)

    led[0] = (0, 0, 0)
    time.sleep(3)

    #----- END LIGHTS ------

    led[0] = (255, 255, 255)
    time.sleep(0.5)

    led[0] = (0,0,0)
    time.sleep(0.5)

    led[0] = (255, 255, 255)
    time.sleep(0.5)

    led[0] = (0,0,0)
    time.sleep(0.5)

    led[0] = (255, 255, 255)
    time.sleep(0.5)

    led[0] = (0,0,0)
    time.sleep(0.5)






