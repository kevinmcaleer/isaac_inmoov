# Isaaca Eyes Client
# listens for commands to make the eyes glow
# Requires the Pimoroni-Pico MicroPython build

from easy_comms import Easy_comms
from time import sleep
import json
import plasma
from plasma import plasma2040

NUM_LEDS = 2
FPS = 60
speed = 10
WAIT = 0.01

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT, rgbw=True, color_order=plasma.COLOR_ORDER_GRB)
led_strip.start(FPS)

def hsv2rgb(hue, sat, val):
    """ Returns the RGB of Hue Saturation and Brightnes values """

    i = math.floor(hue * 6)
    f = hue * 6 - i
    p = val * (1 - sat)
    q = val * (1 - f * sat)
    t = val * (1 - (1 - f) * sat)

    r, g, b = [
        (val, t, p),
        (q, val, p),
        (p, val, t),
        (p, q, val),
        (t, p, val),
        (val, p, q),
    ][int(i % 6)]
    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    
    return r, g, b

def rgb2hsv(r:int, g:int, b:int):
    """ Returns the Hue Saturation and Value of RGB values """
    h = 0
    s = 0
    v = 0
    # constrain the values to the range 0 to 1
    r_normal, g_normal, b_normal,  = r / 255, g / 255, b / 255
    cmax = max(r_normal, g_normal, b_normal)
    cmin = min(r_normal, g_normal, b_normal)
    delta = cmax - cmin
    
    # Hue calculation
    if(delta ==0):
        h = 0
    elif (cmax == r_normal):
        h = (60 * (((g_normal - b_normal) / delta) % 6))
    elif (cmax == g_normal):
        h = (60 * (((b_normal - r_normal) / delta) + 2))
    elif (cmax == b_normal):
        h = (60 * (((r_normal - g_normal) / delta) + 4))
    
    # Saturation calculation
    if cmax== 0:
        s = 0
    else:
        s = delta / cmax
        
    # Value calculation
    v = cmax

    return h, s, v 

def glow():
    hue, sat, val = rgb2hsv(colour['red'], colour['green'], colour['blue'])    
    for i in range(1,100,1):
        value = i/100
        led_strip.set_rgb(colour['red'], colour['green'], colour['blue'])
        led_strip.set_hsv(0,hue,1,value)
        led_strip.set_hsv(1,hue,1,value)
        sleep(WAIT)

    for i in range(100,1,-1):
        value = i/100
        led_strip.set_rgb(colour['red'], colour['green'], colour['blue'])
        led_strip.set_hsv(0,hue,1,value)
        led_strip.set_hsv(1,hue,1,value)
        sleep(WAIT)

com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

# Set the colour to black
colour = {'red':0, 'green':0,'blue':0}

while True:
    message = com1.read()

    if message is not None:
        command = json.loads(message.strip('\n'))
        if command['command'] == 'glow':
            glow(command['args']['red'], command['args']['green'], command['args']['blue'])
