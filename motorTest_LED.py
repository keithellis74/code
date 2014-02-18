#!/usr/bin/env python3
'''Test motor driver with 4 LED's to represent two motors
forward and reverse.

By Keith Ellis

Original version required input from terminal as an input command

Rev 01 - 03/01/2014
Trying input from terminal stdin without haveing to press return
Rev 02 - 07/01/2014
Impliment PWM so that turning is slower and speeed is incremential
Impliment drive_motor() function, this receives ducty cycle and pins to 
set high to drive motors in desired direction
Rev 03 - 10/02/2014
Modify to put PWM on EN pin of L293D driver, and measure volt/currents, 
is it any more efficient - V/Amps no different, but keep PWM on EN 
Rev 04 - 10/02/2014
Add in Threading to detect object ahead and take avoiding action
'''

import RPi.GPIO as GPIO
import time
import sys,tty,termios

''' 	GPIO output pins in pairs are
	Left motor, pins 23 & 7
	Right motor, pins 24 & 8
	L293 EN, pin 22
	IR Sendor, pin 17	
'''
# Setup GPIO output pins
gpio_pins = {'leftMotorPin1' : 23, 'leftMotorPin2' : 7, 'rightMotorPin1' : 24,'rightMotorPin2' : 8}
GPIO.setmode(GPIO.BCM)			# Use BCM pin numbers

# Setup all GPIO pins for output
for pin in gpio_pins:
	GPIO.setup(gpio_pins[pin], GPIO.OUT)

# GPIO pin controlling EN on motor driver, prevents motors running on boot
GPIO.setup(22,GPIO.OUT,initial=0)

# Setup EN pin as PWM
EN = GPIO.PWM(22, 200)
EN.start(0)

# Setup GPIO as input to detect object ahead using IR sensor
ir_sensor = 17
GPIO.setup(ir_sensor, GPIO.IN)

Drive = 0

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


# Stop Function - Sets duty cycle of all pins to zero and sleeps for 0.5 seconds
def stop():
	EN.ChangeDutyCycle(0)
	for pin in gpio_pins:
		GPIO.output(gpio_pins[pin],0)
#	time.sleep(0.2)

# drive_motor fuinction, this takes dc (duty cycle or speed from 0 to 100)
# and motors, this is a LIST detailing which GPIO pins should be set to high
# gpio_pins Dictionary contains four pin numbers 
# left motor forward, left motor revers, right motor forward
# right motor reverse.

def drive_motor(dc,motors):
	stop()
	for pin in motors:
		GPIO.output(gpio_pins[pin], 1)
	for n in range(0,dc+1):	
		EN.ChangeDutyCycle(n)
		time.sleep(0.01)

# Function to take avoiding action if object detected ahead
# running in seperate thread

def object_detect(channel):
	global Drive
	print ("Object_detect drive = ",Drive)
	if Drive == 1:
		avoid_object()
	else:
		pass	

def avoid_object():
	global Drive
	drive_motor(80, ['leftMotorPin2']) 
	while GPIO.input(17) == GPIO.LOW:
		pass
	time.sleep(1)
	print("Stopping")
	print(Drive)
	stop()
	Drive = 0
	print(Drive)

	
#Main code below

stop()
#Call thread to detect object ahead
GPIO.add_event_detect(17, GPIO.FALLING, callback=object_detect,bouncetime=200)
print ("Program Running, use the following keys to control")
print ("1 = Quit \nq = forward\na = reverse\nz = stop\n")
print ("\nu = slow left\n[ = slow right")
print ("o = fast left\np = fast right")
while True:
	try:
		n = getch()
		n = n.lower()

		if n == "q":		# Forwards
			global Drive
			Drive = 1
			drive_motor(100,['leftMotorPin1','rightMotorPin1'])

		elif n == "a":		# Reverse
			drive_motor(100,['leftMotorPin2','rightMotorPin2'])

		elif n == "o":		# fast Left
			drive_motor(80,['leftMotorPin2','rightMotorPin1'])

		elif n == "p":		# fast Right
			drive_motor(80,['leftMotorPin1','rightMotorPin2'])

		elif n == "z":		# stop
			stop()

		elif n == "i":		# slow Left
			drive_motor(80,['rightMotorPin1'])

		elif n == "[":		# slow Right
			drive_motor(80,['leftMotorPin1'])

		elif n == "1": 
			print ("Program Ended")
			GPIO.cleanup()
			break
	
		n=""

	except (KeyboardInterrupt):
		GPIO.cleanup()
		break
