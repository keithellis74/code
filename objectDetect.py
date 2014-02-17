#!//urs/bin/env python3
#K Ellis 10/02/2014
# Program to test IR object dection sensor on BCM pin 17

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  #Use BCM pin numbers
GPIO.setup(17, GPIO.IN)

while True:
	try:
		if GPIO.input(17) == GPIO.LOW:
			print ("Object")
		else:
			print ("No Object")
	except keyboardinterupt:
		GPIO.cleanup() 

