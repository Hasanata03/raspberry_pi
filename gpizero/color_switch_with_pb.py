from gpiozero import LED, Button
import time
from signal import pause

red = LED(23)
yellow = LED(24)
green = LED(25)
button = Button(16 , bounce_time=(0.03))

red.on()

count = 0

def switch(ev = None):
    global count
    count += 1
    
    if count % 3 == 0:
        print("Red Led turned on\tCount:" + str(count))
        red.on()
        yellow.off()
        green.off()
    elif count % 3 == 1:
           print("Yellow Led turned on\tCount:" + str(count))
           red.off()
           yellow.on()
           green.off()
    elif count % 3 == 2:
         print("Green Led turned on\tCount:" + str(count))
         red.off()
         yellow.off()
         green.on()

button.when_pressed = switch

pause()
