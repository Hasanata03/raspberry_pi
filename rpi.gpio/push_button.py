import RPi.GPIO as GPIO
import time

BUTTON = 18
LED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED , GPIO.OUT)
GPIO.setup(BUTTON , GPIO.IN)


while True:
    time.sleep(0.01)
    if GPIO.input(BUTTON) == GPIO.HIGH:
        GPIO.output(LED , GPIO.HIGH)
    else:
        GPIO.output(LED , GPIO.LOW)
        
        
        
GPIO.cleanup()
      