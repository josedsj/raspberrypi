# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:16:32 2020

@author: jd
"""


import RPi.GPIO as GPIO
import time
import dht11
import time
import datetime
from time import sleep
# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)
buzzTime=0.2
buzzDelay=2
buzzerPin = 26 #select the pin for buzzer
GPIO.setup(instance,GPIO.IN)
GPIO.setup(buzzerPin,GPIO.OUT)

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))
	        print("Temperature: %-3.1f C" % result.temperature)
	        print("Humidity: %-3.1f %%" % result.humidity)
            GPIO.output(buzzerPin, True)
            sleep(buzzTime)
            GPIO.output(buzzerPin, False)
	    time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
    