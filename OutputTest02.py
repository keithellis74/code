###############################################
### Testing Outputs on the Raspberry Pi     ###
###            Version 02                   ###
### In this version -                       ###
### Set Pins to False before excecuting     ###
### any code                                ###
###                                         ###
###                                         ###
###############################################

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)                    #use BCM numbers

pin1 = 23				#setup variables for pin
pin2 = 7				# numbers

GPIO.setup(pin1, GPIO.OUT)                  #setup pin 1 as output
GPIO.setup(pin2, GPIO.OUT)                  #setup pin 2 as output

GPIO.output(pin1 , False)			#Set pin 1 to off (false)
GPIO.output(pin2 , False)			#Set pin 2 to off (false)
while True:                               #This while statement works but raw_input is better
	print ("Pin1 = ", GPIO.input(pin1))
	print ("Pin2 = ", GPIO.input(pin2))
   
	n = input("\n\nPress 1 to toggle pin 1 or 2 to toggle pin 2:\nPress q to quit\n") # than input. Find out how to use raw_input
	if n.strip() == "1":
		GPIO.output(pin1, not GPIO.input(pin1))      

	elif n.strip() == "2":
		GPIO.output(pin2, not GPIO.input(pin2))

	elif n.strip() == "3":
		GPIO.output(pin1, not GPIO.input(pin1))
		GPIO.output(pin2, not GPIO.input(pin2))

	elif n.strip() =="q": break ### This is not working, the GPIO.cleanup() sttement is not running
	elif n.strip() =="Q": break

#GPIO.output(11, False)
#GPIO.output(12, False)
#print ("Pin 1 before quiting = ", GPIO.input(pin1))
#print ("Pin 2 before quiting = ", GPIO.input(pin2))
GPIO.cleanup()
