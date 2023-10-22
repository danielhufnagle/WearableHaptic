# PULSE WIDTH MODULATION WITH SHIFT REGISTER

# import dependencies
import RPi.GPIO as GPIO
from time import sleep

# set pin numbering system
GPIO.setmode(GPIO.BCM)

# setup data, latch, clock pins
PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21
GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

GPIO.setwarnings = False

# set pattern for the LEDs, 1 is on 0 is off
ledpattern = [1, 1, 1, 1, 1, 1, 1, 1]

# manual pulse width modulation
while True:
    try:
        # light up LEDS according to pattern
        for i in range(len(ledpattern)):
            GPIO.output(PIN_DATA, ledpattern[i])
            GPIO.output(PIN_CLOCK, 1)
            GPIO.output(PIN_CLOCK, 0)
        GPIO.output(PIN_LATCH, 1)
        GPIO.output(PIN_LATCH, 0)
        # turn off LEDS
        for i in range(len(ledpattern)):
            GPIO.output(PIN_DATA, 0)
            GPIO.output(PIN_CLOCK, 1)
            GPIO.output(PIN_CLOCK, 0)
        GPIO.output(PIN_LATCH, 1)
        GPIO.output(PIN_LATCH, 0)
        # set sleep period between darkening and lighting... Longer sleep means "dimmer LEDs"
        sleep(0)
    except KeyboardInterrupt:
        break
