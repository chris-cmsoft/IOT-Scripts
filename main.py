import atexit
import time
import RPi.GPIO as GPIO
from multiprocessing import Process

def cleanupGpio():
    print ('cleaning up ...')
    GPIO.cleanup();

atexit.register(cleanupGpio)

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def lightsarray1():
    current = 2
    while True:
        if current == 4:
            current = 2
        else:
            current = current+1
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(current, GPIO.HIGH)
        time.sleep(0.1)

def lightsarray2():
    current = 14
    while True:
        if current == 18:
            current = 14
        elif current == 14:
            current = 15
        else:
            current = 18
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(current, GPIO.HIGH)
        time.sleep(0.3)

# Start Process to start first array of lights
p1 = Process(target=lightsarray1)
p1.start()

# Start Process to start second array of lights
p2 = Process(target=lightsarray2)
p2.start()

while True:
    print GPIO.input(21)
    print GPIO.input(20)
    time.sleep(1)

# Exit the program
exit
