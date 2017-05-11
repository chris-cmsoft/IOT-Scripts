import atexit
import time
import RPi.GPIO as GPIO  

def cleanupGpio():
    GPIO.cleanup();

atexit.register(cleanupGpio)

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

if __name__ == '__main__':
    
    current = 2
    while True:

        if current == 4:
            current = 2
        else:
            current = current+1
        GPIO.output(2, GPIO.OUT)
        GPIO.output(3, GPIO.OUT)
        GPIO.output(4, GPIO.OUT)
        GPIO.output(current, current)
        time.sleep(0.1)
