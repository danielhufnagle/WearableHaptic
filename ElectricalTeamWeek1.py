import RPi.GPIO as GPIO
from time import sleep

def blink(pin_num):
    GPIO.output(pin_num, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin_num, GPIO.LOW)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)

while True:
    blink(7)
    blink(11)
    blink(13)
    blink(15)
    blink(29)
    blink(31)
    blink(33)
    blink(35)