from time import sleep
import numpy as np
import gpiozero

# create the message and convert it (if needed) to 0 and 1
message = np.zeros(5000)
for i in range(message.size):
  if (i % 2) == 0:
    message[i] = 1
# print(message)

# declare the connection (you have to connect the led to a GPconnection)
led = gpiozero.LED(17)

space_time = 0.0003
# send the message
led.on() #beginning signal
sleep(5)
for i in range(message.size):
  if message[i] == 1:
    led.on()
  else:
    led.off()
  sleep(space_time)