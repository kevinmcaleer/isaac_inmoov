# Isaaca Eyes Client
# listens for commands to make the eyes glow

from easy_comms import Easy_comms
from time import sleep
import json

com1 = Easy_comms(uart_id=0, baud_rate=9600)
com1.start()

while True:
    message = com1.read()

    if message is not None:
        command = json.loads(message.strip('\n'))
        if command['command'] == 'glow':
            eyes.glow(command['args']['red'], command['args']['green'], command['args']['blue'])