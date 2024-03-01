import RPi.GPIO as GPIO
import time

BeepPin = 11  # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(BeepPin, GPIO.OUT)  # Set BeepPin's mode to output
    GPIO.output(BeepPin, GPIO.HIGH)  # Set BeepPin high (+3.3V) to turn off beep

def loop():
    while True:
        GPIO.output(BeepPin, GPIO.LOW)  # Switch on Buzzer
        time.sleep(0.3)  # 0.3s delay
        GPIO.output(BeepPin, GPIO.HIGH)
        time.sleep(0.3)

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)  # Turn off the beep
    GPIO.cleanup()  # Release resources
    print('Program terminated.')

print('Press Ctrl+C to end the program...')
setup()

try:
    loop()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    destroy()
