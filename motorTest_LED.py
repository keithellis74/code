import RPi.GPIO as GPIO
import time

''' 	GPIO output pins in pairs are
	Left motor, pins 23 & 7
	Right motor, pins 24 & 8
'''

gpio_pins = {'leftMotorPin1' : 23, 'leftMotorPin2' : 7, 'rightMotorPin1' : 24,'rightMotorPin2' : 8}

# Setup GPIO output pins

GPIO.setmode(GPIO.BCM)			# Use BCM pin numbers


''' Setup all GPIO pins for output '''

for number in gpio_pins:
	GPIO.setup(gpio_pins[number], GPIO.OUT)


''' Functions to control movement of robot.  Inc. stop, forward,
 reverse, fast left, fast right, slow left, slow right '''


def stop():
	for number in gpio_pins:
		GPIO.output(gpio_pins[number], False)


def forward():
	stop()
	GPIO.output(gpio_pins['leftMotorPin1'], True)
	GPIO.output(gpio_pins['rightMotorPin1'], True)

def reverse():
	stop()
	GPIO.output(gpio_pins['leftMotorPin2'], True)
	GPIO.output(gpio_pins['rightMotorPin2'], True)


def fastLeft():
	stop()
	GPIO.output(gpio_pins['rightMotorPin1'], True)
	GPIO.output(gpio_pins['leftMotorPin2'], True)

def fastRight():
	stop()
	GPIO.output(gpio_pins['leftMotorPin1'], True)
	GPIO.output(gpio_pins['rightMotorPin2'], True)

def slowLeft():
	stop()
	GPIO.output(gpio_pins['rightMotorPin1'], True)

def slowRight():
	stop()
	GPIO.output(gpio_pins['leftMotorPin1'], True)

	

stop()
while True:
	n = input("press q for forward\na for reverse\no for fast letf\np for fast right\n")
	n = n.lower()

	if n == "q":
		forward()

	elif n == "a":
		reverse()

	elif n == "o":
		fastLeft()

	elif n == "p":
		fastRight()

	elif n == "z":
		stop()

	elif n == "i":
		slowLeft()

	elif n == "[":
		slowRight()

	elif n == "1": 
		break


GPIO.cleanup()

