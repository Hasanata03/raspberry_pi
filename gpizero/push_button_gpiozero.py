from gpiozero import LED, Button
import time
from signal import pause

led = LED(23)
button = Button(16)

button.when_pressed = led.on
button.when_released = led.off

pause()
# while True:
#     if button.is_pressed:
#         led.on()
#     else:
#         led.off()
#     time.sleep(0.03)        