import RPi.GPIO as GPIO
import time

BeepPin = 38  # Pin 38

def setup():
    GPIO.setmode(GPIO.BOARD)        # Use physical pin numbering
    GPIO.setup(BeepPin, GPIO.OUT)   # Set BeepPin as output
    GPIO.output(BeepPin, GPIO.HIGH) # Turn off the beep initially

def loop():
    try:
        while True:
            GPIO.output(BeepPin, GPIO.LOW)   # Turn on the buzzer
            time.sleep(0.1)                  # 0.1s delay
            GPIO.output(BeepPin, GPIO.HIGH)  # Turn off the buzzer
            time.sleep(0.1)
    except KeyboardInterrupt:  # When Ctrl+C is pressed, the program will exit the loop
        destroy()

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)    # Turn off the beep
    GPIO.cleanup()                     # Clean up GPIO resources

print('Press Ctrl+C to end the program...')

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
