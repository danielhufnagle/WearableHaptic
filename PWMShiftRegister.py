# PULSE WIDTH MODULATION WITH SHIFT REGISTER

# import dependencies
import RPi.GPIO as GPIO
# set pin numbering system to BCM
GPIO.setmode(GPIO.BCM)

# declare and set up data, latch, clock pins
PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21

GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

# turn off warnings
GPIO.setwarnings(False)

# set led pattern (1 is on, 0 is off - be aware this might be "backwards")
ledpattern = '00100111'

# start PWM instance with frequency
pwm_inst = GPIO.PWM(PIN_DATA, 1000)

GPIO.output(PIN_LATCH, 0)

# light up the LEDs - hopefully
for x in range(len(ledpattern)):
    # if the led is to be lit, marked by 1 in ledpattern
    if ledpattern[x] == "1":
        # gradually brightens the LED
        for duty in range(0, 101):
            pwm_inst.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.01)
        # gradually darkens the LED
        for duty in range(100, -1, -1):
            pwm_inst.ChangeDutyCycle(duty)
            sleep(0.01)
    # if the led is not to be lit, marked by 0 in ledpattern
    else:
        GPIO.output(PIN_DATA, 0) # this might not work
        # if the code doesn't work then comment out the previous line and uncomment the following line
        # pwm_inst.ChangeDutyCycle(0)
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)

GPIO.output(PIN_LATCH, 1)