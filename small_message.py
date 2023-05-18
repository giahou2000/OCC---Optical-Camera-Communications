from time import sleep
import numpy as np
import gpiozero

# create the message and convert it (if needed) to 0 and 1
message = np.zeros(500)
for i in range(message.size):
  if (i % 2) == 0:
    message[i] = 1
# print(message)

# declare the connection (you have to connect the led to a GPIO connection)
led = gpiozero.LED(17)

space_time = 0.0003
led.off()
# send the message
led.on()
sleep(10)
led.off()
sleep(5)
for i in range(0, message.size, 2):
  for _ in range(68):
    for j in range(i, i+2):
      if j < message.size:
        if message[j] == 1:
          led.on()
        else:
          led.off()
        sleep(space_time)