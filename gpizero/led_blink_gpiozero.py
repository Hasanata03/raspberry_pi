from gpiozero import LED
import time

led = LED(23)

while True:

  led.on()
  time.sleep(0.5)
  led.off()
  time.sleep(0.5)