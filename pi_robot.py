#!/usr/bin/env python
''' 	Pi Robot main code
	Motor driver for two motors forward and reverse.
	Object advoidance with two IR sensors, one front left
	and another front right

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
Rev 05 - 25/02/2014
Add second thread to detect front left and front right using two object
detection IR sensors
Rev 06 - 13/03/2014
Start to impliment Wii Remote control (buttons only)
'''

import RPi.GPIO as GPIO
import time
import sys,tty,termios
import cwiid 		# Requied for Wii Remote

''' 	GPIO output pins in pairs are (using BCM pin numbers)
	Left motor, pins 23 & 7
	Right motor, pins 24 & 8
	L293 EN, pin 22
	IR Sensor front left, pin 17
	IR Sensor front right, pin 27
	Also used by Arduino Teensy for I2C pins 2 & 3 	
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
ir_sensor_fl = 17
ir_sensor_fr = 27
GPIO.setup(ir_sensor_fl, GPIO.IN)
GPIO.setup(ir_sensor_fr, GPIO.IN)

# Global variable, 0 at all times except when driving forward then = "forward"
# Used in object detect interupt to ensure it is only active when driving
# forward
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

# drive_motor fuinction, this takes dc (duty cycle or speed from 0 to 100)
# and motors, this is a LIST detailing which GPIO pins should be set to high
# gpio_pins Dictionary contains four pin numbers 
# left motor forward, left motor revers, right motor forward
# right motor reverse.

def drive_motor(dc,motors):
#	stop()
	for pin in motors:
		GPIO.output(gpio_pins[pin], 1)
#	for n in range(0,dc+1):	
		EN.ChangeDutyCycle(dc)
#		time.sleep(0.01)

# Function to take avoiding action if object detected ahead
# running in seperate thread

def object_detect(channel):
	global Drive
	if Drive == "forward":
		avoid_object_forward(channel)

def avoid_object_forward(sensor):
	global Drive
	if sensor == ir_sensor_fl:
		drive_motor(80, ['rightMotorPin2']) 
		while GPIO.input(ir_sensor_fl) ==GPIO.LOW or GPIO.input(ir_sensor_fr) == GPIO.LOW:
			pass
		time.sleep(0.2)
		drive_motor(100, ['leftMotorPin1','rightMotorPin1'])
		#stop()
		#Drive = 0
	else:
		drive_motor(80, ['leftMotorPin2'])
		while GPIO.input(ir_sensor_fl) ==GPIO.LOW or GPIO.input(ir_sensor_fr) == GPIO.LOW:
			pass
		time.sleep(0.2)
		drive_motor(100, ['leftMotorPin1','rightMotorPin1'])
		#stop()
		#Drive = 0


	
#Main code below

stop()
# Search for Wii Remote
print "Press 1 + 2 on your Wii Remote now..."
time.sleep(1)

#Connect to the Wii Remote.  If it times out then quit.
try:
	wii=cwiid.Wiimote()
	wiimote=True
	wii.rpt_mode = cwiid.RPT_BTN
except RuntimeError():
	print "Error opening wiimote connection"
	print "Use keys to control"
	wiimote = False

#Call thread to detect object ahead
GPIO.add_event_detect(ir_sensor_fl, GPIO.FALLING, callback=object_detect)
GPIO.add_event_detect(ir_sensor_fr, GPIO.FALLING, callback=object_detect)

# Display keyboard commands on the screen and detect key presses
print "Program Running, use the following keys to control"
print "1 = Quit \nq = forward\na = reverse\nz = stop\n"
print "\nu = slow left\n[ = slow right"
print "o = fast left\np = fast right"

print "wiimote = ",wiimote
if wiimote == True:
	while wiimote == True:
		buttons = wii.state["buttons"]
		print buttons
		# If Plus and Minus buttons pressed
		# together then rumble and quit.
		if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
			print "\nClosing connection ..."
			wii.rumble = 1
			time.sleep(1)
			wii.rumble = 0
			wiimote = False
			#exit(wii)

		elif(buttons & cwiid.BTN_UP):  #  Forwards
			print "forward"
			Drive = "forward"
			drive_motor(100,['leftMotorPin1','rightMotorPin1'])
		elif(buttons & cwiid.BTN_DOWN):  #  Reverse
			print "reverse"
			Drive = 0
			drive_motor(100,['leftMotorPin2','rightMotorPin2'])
		elif(buttons == 256):  #  Slow Left
                        print "slow left"
                        Drive = "forward"
                        drive_motor(100,['rightMotorPin1'])
                elif(buttons == 512):  #  Slow right
                        print "slow right"
                        Drive = 0
                        drive_motor(100,['leftMotorPin1'])
		elif(buttons == 260):  #  Fast left
                        print "Fast left"
                        Drive = "forward"
                        drive_motor(100,['leftMotorPin2','rightMotorPin1'])
                elif(buttons == 516):  #  Fast right
                        print "Fast right"
                        Drive = 0
                        drive_motor(100,['leftMotorPin1','rightMotorPin2'])

		else:
			stop()

elif wiimote == False:
	while True:
		try:
			n = getch()
			n = n.lower()

			if n == "q":		# Forwards
				Drive = "forward"
				drive_motor(100,['leftMotorPin1','rightMotorPin1'])

			elif n == "a":		# Reverse
				Drive = 0
				drive_motor(100,['leftMotorPin2','rightMotorPin2'])

			elif n == "o":		# fast Left
				Drive = 0
				drive_motor(100,['leftMotorPin2','rightMotorPin1'])

			elif n == "p":		# fast Right
				Drive = 0
				drive_motor(100,['leftMotorPin1','rightMotorPin2'])

			elif n == "z":		# stop
				Drive = 0
				stop()

			elif n == "i":		# slow Left
				Drive = 0
				drive_motor(100,['rightMotorPin1'])

			elif n == "[":		# slow Right
				Drive = 0
				drive_motor(100,['leftMotorPin1'])

			elif n == "1": 
				print ("Program Ended")
				GPIO.cleanup()
				break
	
			n=""

		except (KeyboardInterrupt):
			GPIO.cleanup()
			break


GPIO.cleanup()
