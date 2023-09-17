# On-board LED Homework for Desert Media Art
# Ronit Singh
# 2023-09-17

import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 1

# changing LED colors based on country flags
while True:
    # india flag
    led[0] = (255,69,0) # orange
    time.sleep(1)
    led[0] = (0,0,255) # blue
    time.sleep(1)
    led[0] = (0, 128, 0) # green
    time.sleep(1)

    # showing no color to separate next flag
    led[0] = (0, 0, 0)
    time.sleep(1)

    # uae flag
    led[0] = (255, 0, 0) # red
    time.sleep(1)
    led[0] = (0, 128, 0) # green
    time.sleep(1)
    led[0] = (255,255,255) # white
    time.sleep(1)

    # showing no color to separate next flag
    led[0] = (0, 0, 0)
    time.sleep(1)

    #australia flag
    led[0] = (255, 0, 0) # red
    time.sleep(1)
    led[0] = (0,0,255) # blue
    time.sleep(1)
    led[0] = (255,255,255) # white
    time.sleep(1)

    # showing no color to separate next flag
    led[0] = (0, 0, 0)
    time.sleep(1)

    #singapore flag
    led[0] = (255, 0, 0) # red
    time.sleep(1)
    led[0] = (255,255,255) # white
    time.sleep(1)

    # showing no color to separate next flag
    led[0] = (0, 0, 0)
    time.sleep(1)

    #united states flag
    led[0] = (255, 0, 0) # red
    time.sleep(1)
    led[0] = (0,0,255) # blue
    time.sleep(1)
    led[0] = (255,255,255) # white
    time.sleep(1)

    # showing no color to separate next flag
    led[0] = (0, 0, 0)
    time.sleep(3)

    #----------time variations-------------

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

    #----------time variations-------------

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
