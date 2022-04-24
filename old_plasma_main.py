from servo import Servo, servo2040
from time import sleep

from plasma import WS2812 
# Create the LED bar, using PIO 1 and State Machine 0
led_bar = WS2812(servo2040.NUM_LEDS, 1, 0, servo2040.LED_DATA)

# Start updating the LED bar
led_bar.start()

BRIGHTNESS = 0.5

while True:
    for j in range(0,100,1):
        for i in range(servo2040.NUM_LEDS):
            led_bar.set_hsv(i,j/100,1,BRIGHTNESS)
            print(f"J is {j}, i is {i}")
        sleep(0.01)
    

eyes_left_right = Servo(servo2040.SERVO_2)
eyes_up_down = Servo(servo2040.SERVO_1)
neck = Servo(servo2040.SERVO_3)
sonny = Servo(servo2040.SERVO_18)

eyes_left_right.to_mid()
eyes_up_down.to_mid()
sonny.to_mid()
# neck.to_mid()

WAIT = 0.01

sleep(WAIT)

# for i in range(-80, 80,1):
#     neck.value(i)
#     sleep(WAIT)

# while True:
#     sonny.to_min()
#     sleep(0.25)
#     sonny.to_mid()
#     sleep(0.1)
#     sonny.to_min()
#     sleep(0.25)
#     sonny.to_mid()
#    
#     sleep(1)
# 
# while True:
#     for i in range (-40,40,1):
#         eyes_left_right.value(i)
#         sonny.value(i)
#         print(i)
#         sleep(WAIT)
#     for i in range (40,-40,-1):
#         eyes_left_right.value(i)
#         sonny.value(i)
#         sleep(WAIT)
#     
# for i in range(-50,50,1):
#     eyes_up_down.value(i)
#     sleep(WAIT)
   
eyes_left_right.disable()
eyes_up_down.disable()
neck.disable()
