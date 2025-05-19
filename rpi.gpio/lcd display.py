from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
from time import sleep


# LCD'yi Raspberry Pi'ye ba?l?yoruz (Paralel Mod - 4 Bit)
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=25, pin_e=24, pins_data=[23, 18, 15, 14])

# LCD'ye metin yazd?rma
lcd.clear()
lcd.write_string("Raspberry Pi 5!")

sleep(3)