import RPi.GPIO as GPIO
import time

led_state = False
count = 0

BUTTON = 16
LED = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED , GPIO.OUT)
GPIO.setup(BUTTON , GPIO.IN)


def switch(ev = None):
    global led_state, count
    led_state = not led_state
    count += 1
    
    if led_state == True:
        print("Led turned on\tCount:" + str(count))
        GPIO.output(LED , GPIO.HIGH)

    else:
           print("Led turned off\tCount:" + str(count))
           GPIO.output(LED , GPIO.LOW)  




def detect_button_push():
    GPIO.add_event_detect(BUTTON , GPIO.FALLING , callback= switch , bouncetime=300 )

def wait():
     while True:
          time.sleep(0.01)


detect_button_push()
wait()    