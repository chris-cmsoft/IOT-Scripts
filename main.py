import atexit
import time
import RPi.GPIO as GPIO
from multiprocessing import Process, Value, Pipe

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
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def lightsarray1(speed = None):
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
        time.sleep(speed.value)

def lightsarray2(speed = None):
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
        time.sleep(speed.value)

def printValues(speed1, speed2):
    first = True
    while True:
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        if first:
            print('Light array 1: ' + str(p1Speed.value) + '\tLight array 2: ' + str(p2Speed.value))
        else:
            print(CURSOR_UP_ONE + ERASE_LINE + 'Light array 1: ' + str(p1Speed.value) + '\tLight array 2: ' + str(p2Speed.value))
        time.sleep(0.1)
        if first:
            first = False

p1Speed = Value('d', 1)
p2Speed = Value('d', 3)

# Start Process to start first array of lights
p1 = Process(target=lightsarray1, args=(p1Speed,))
p1.start()

# Start Process to start second array of lights
p2 = Process(target=lightsarray2, args=(p2Speed,))
p2.start()

Process(target=printValues, args=(p1Speed, p2Speed, )).start()

p1ButtonValue = 0
p2ButtonValue = 0
p3ButtonValue = 0

while True:
    if GPIO.input(21) == 1 and p1ButtonValue == 0:
        p1Speed.value = p1Speed.value - (p1Speed.value / 5)
    if GPIO.input(20) == 1 and p2ButtonValue == 0:
        p2Speed.value = p2Speed.value - (p2Speed.value / 5)
    if GPIO.input(16) == 1 and p3ButtonValue == 0:
        p2Speed.value = 1
        p1Speed.value = 3
    p1ButtonValue = GPIO.input(21)
    p2ButtonValue = GPIO.input(20)
    p3ButtonValue = GPIO.input(16)

# Exit the program
exit
