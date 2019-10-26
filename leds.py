#!/usr/bin/env python3
import RPi.GPIO as GPIO, sys, signal, time, random

verbose = None
leds = None
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

class LED():
    """Access the LEDs with simple methods."""
    global verbose

    def __init__(self, pin):
        self.pin = pin
        global leds
        leds.append(self)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self, count):
        if verbose: print('Start blink')