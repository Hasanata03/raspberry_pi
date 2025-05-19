from gpiozero import LED, Button
import time
from signal import pause

led = LED(23)
button = Button(16 , bounce_time=(0.03))

led_state = False
count = 0

def switch(ev = None):
    global led_state, count
    led_state = not led_state
    count += 1
    
    if led_state == True:
        print("Led turned on\tCount:" + str(count))
        led.on()
    else:
           print("Led turned off\tCount:" + str(count))
           led.off()

button.when_pressed = switch
