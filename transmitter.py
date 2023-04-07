from time import sleep
import numpy as np
import gpiozero


start_sequence = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
end_sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# create the message and convert it (if needed) to 0 and 1
message = np.zeros(1000000)
for i in range(message.size):
  if (i % 2) == 0:
    message[i] = 1
# print(message)

# declare the connection (you have to connect the led to a GPconnection)
led = gpiozero.LED(17)

space_time = 0.0003
led.off()
# send the message
for i in range(len(start_sequence)):
  if start_sequence[i] == 1:
    led.on()
  else:
    led.off()
  sleep(space_time)
for i in range(message.size):
  if message[i] == 1:
    led.on()
  else:
    led.off()
  sleep(space_time)
for i in range(len(end_sequence)):
  if end_sequence[i] == 1:
    led.on()
  else:
    led.off()
  sleep(space_time)