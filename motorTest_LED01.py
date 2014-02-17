'''Test motor driver with 4 LED's to represent two motors
forward and reverse.

By Keith Ellis

Original version required input from terminal as an input command

Rev 01 - 03/01/2014
Trying input from terminal stdin without haveing to press return
'''



import RPi.GPIO as GPIO
import time
import sys,tty,termios

''' 	GPIO output pins in pairs are
	Left motor, pins 23 & 7
	Right motor, pins 24 & 8
'''
# Setup GPIO output pins
 
gpio_pins = {'leftMotorPin1' : 23, 'leftMotorPin2' : 7, 'rightMotorPin1' : 24,'rightMotorPin2' : 8}


GPIO.setmode(GPIO.BCM)			# Use BCM pin numbers


''' Setup all GPIO pins for output '''

for number in gpio_pins:
	GPIO.setup(gpio_pins[number], GPIO.OUT)


''' Functions to control movement of robot.  Inc. stop, forward,
 reverse, fast left, fast right, slow left, slow right '''


# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

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
print ("Program Running, use the following keys to control")
print ("1 = Quit \nq = forward\na = reverse\nz = stop\n")
print ("\nu = slow left\n[ = slow right")
print ("o = fast left\np = fast right")
while True:
	n = getch()
#	n = input("press q for forward\na for reverse\no for fast letf\np for fast right\n")
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
		print ("Program Ended")
		break
	n=""

GPIO.cleanup()

