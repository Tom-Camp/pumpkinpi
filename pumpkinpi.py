#!/usr/bin/env python3
import RPi.GPIO as GPIO, time, sys, datetime

verbose = None
debug = None

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
motionsensor = 17
GPIO.setup(motionsensor, GPIO.IN)

class LED:
    """Acces the LEDS"""
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        leds.append(self)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self, count):
        x = 0
        while x <= count:
            GPIO.output(self.pin, True)
            time.sleep(.1)
            GPIO.output(self.pin, False)
            x = x + 1

leds = []

eyeOne = LED(20, 'Eye One')
eyeTwo = LED(21, 'Eye Two')
yellow = LED(22, 'Yellow')
white = LED(23, 'White')
bigYellow = LED(24, 'Big Yellow')
bigWhite = LED(25, 'Big White')

def all_on():
    for i in range(len(leds)):
        leds[i].on()

def all_off():
    for i in range(len(leds)):
        leds[i].off()

def open_eyes():
    eyeOne.on()
    eyeTwo.on()

def close_eyes():
    eyeOne.off()
    eyeTwo.off()

def blink_sequence():
    for i in range(len(leds)):
        leds[i].blink(10)

def pumpkin_pi_quit():
    all_off()
    GPIO.cleanup()
    sys.exit(0)

def debug_leds():
    global debug
    debug = True
    func_list = {
        1 : ['Eye #1', eyeOne.on],
        2 : ['Eye #2', eyeTwo.on],
        3 : ['Yellow', yellow.on],
        4 : ['White', white.on],
        5 : ['Big Yellow', bigYellow.on],
        6 : ['Big Whte', bigWhite.on],
        7 : ['All on', all_on],
        8 : ['All Off', all_off],
        9 : ['Quit', pumpkin_pi_quit]}

    for i in range(1, len(func_list) + 1):
    	print('{}: {}'.format(i, func_list[i][0]))

    x = int(input('Select function => '))
    try:
        func_list[x][1]()
    except ValueError:
        print('No valid input.')
    debug_leds()

def motion_sensor():
    last_motion = None
    while True:
        if GPIO.input(motion_sensor):
            last_motion = datetime.datetime.now()
            blink_sequence()
        else:
            if datetime.datetime.now() > last_motion + 60:
                all_off()


def main():
    global verbose
    verbose = False
    global debug
    debug = False

    if '-v' in sys.argv:
        verbose = True

    if '-d' in sys.argv:
        debug_leds()

    motion_sensor()

if __name__ == '__main__':
    print('Motion Sensing')
    main()

