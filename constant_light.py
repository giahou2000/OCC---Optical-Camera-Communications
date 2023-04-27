from time import sleep
import numpy as np
import gpiozero

# declare the connection (you have to connect the led to a GPIO connection)
led = gpiozero.LED(17)

led.on()
sleep(1000)