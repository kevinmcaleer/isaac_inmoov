# Isaaca Eyes Neopixels
# Kevin McAleer
# 24 April 2022

import plasma
from plasma import plasma2040
from time import sleep
from random import choice

NUM_LEDS = 2
FPS = 60
speed = 10
WAIT = 0.01

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT, rgbw=True, color_order=plasma.COLOR_ORDER_GRB)
led_strip.start(FPS)

RED = 1.0
BLUE = 0.6
GREEN = 0.3
PINK = 0.9

colours = [RED,BLUE,GREEN,PINK]

def red_glow():
    
    eyes = choice(colours)
    for i in range(1,100,1):
        value = i/100
        led_strip.set_hsv(0,eyes,1,value)
        led_strip.set_hsv(1,eyes,1,value)
        sleep(WAIT)

    for i in range(100,1,-1):
        value = i/100
        led_strip.set_hsv(0,eyes,1,value)
        led_strip.set_hsv(1,eyes,1,value)
        sleep(WAIT)

while True:
    red_glow()
