import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 17

GPIO.setup(LED , GPIO.OUT)

while True:
    GPIO.output(LED , GPIO.HIGH)
    time.sleep(1)
GPIO.output(LED , GPIO.LOW)
time.sleep(1)


GPIO.cleanup()