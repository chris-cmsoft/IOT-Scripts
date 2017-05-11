import atexit
import time
import RPi.GPIO as GPIO  

def cleanupGpio():
    GPIO.cleanup();

atexit.register(cleanupGpio)

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    GPIO.setup(2, GPIO.OUT)
    current = True
    while True:
       GPIO.output(2, current)
       current = not current
       time.sleep(1)
