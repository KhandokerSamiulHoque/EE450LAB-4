import RPi.GPIO as GPIO
import time

BeepPin = 38
LedPin = 40

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BeepPin, GPIO.OUT)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.output(LedPin, GPIO.LOW)

def loop():
    try:
        while True:
            GPIO.output(BeepPin, GPIO.LOW)
            GPIO.output(LedPin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(BeepPin, GPIO.HIGH)
            GPIO.output(LedPin, GPIO.LOW)
            time.sleep(0.2)
    except KeyboardInterrupt:
        destroy()

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

print('Press Ctrl+C to end the program...')

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()

