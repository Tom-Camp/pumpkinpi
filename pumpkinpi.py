#!/usr/bin/env python3
from leds import LED
import RPi.GPIO as GPIO, sys

verbose = None
debug = None
leds = []

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
motionsensor = 17
GPIO.setup(motionsensor, GPIO.IN)

eyeOne = LED(20)
eyeTwo = LED(21)
yellow = LED(22)
white = LED(23)
bigYellow = LED(24)
bigWhite = LED(25)

def all_off():
    for i in range(len(leds)):
        leds[i].on()

def all_on():
    for i in range(len(leds)):
        leds[i].off()

def debug_leds():
    """Function for debugging LEDs"""
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
        9 : ['Quit', sys.exit]}

    for i in range(1, len(func_list) + 1):
        print('{}: {}'.format(i, func_list[i][0]))

    x = int(input('Select function => '))

    try:
        func_list[x][1]()
    except ValueError:
        print('Message: {}'.format(ValueError.message))
    finally:
        debug_leds()

def main():
    global verbose
    verbose = False
    global debug
    debug = False

    if '-v' in sys.argv:
        verbose = True

    if '-d' in sys.argv:
        debug_leds()

if __name__ == '__main__':
    print('Pumpkin Pi starting')
    main()