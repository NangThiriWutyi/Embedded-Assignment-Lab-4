import RPi.GPIO as GPIO
import time

BeepPin = 11  # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(BeepPin, GPIO.OUT)  # Set BeepPin's mode is output
    GPIO.output(BeepPin, GPIO.LOW)  # Set BeepPin low to turn off the beep initially

def loop():
    while True:
        GPIO.output(BeepPin, GPIO.HIGH)  # Switch off Buzzer
        time.sleep(0.5)  # 0.5s delay
        GPIO.output(BeepPin, GPIO.LOW)  # Switch on Buzzer
        time.sleep(0.5)

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)  # Turn off the beep
    GPIO.cleanup()  # Release resources
    print('Program terminated.')

print('Press Ctrl+C to end the program...')
setup()

try:
    loop()
except KeyboardInterrupt:
    destroy()
