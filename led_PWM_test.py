###############################################
### LED Pulse Width Modulation Test         ###
###            Version 00                   ###
### 28 December 2013                        ###
### In this version -                       ###
###                                         ###
### Turn LED's on and then dim them         ###
###                                         ###
###                                         ###
###############################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)                  #use BCM numbers

pin1 = 23		# Original 23	     	# setup variables for pin
pin2 = 7		# Original 7
				# numbers
frequency = 100				# PWM frequency
dc = 0					# PWM Duty Cycle

GPIO.setup(pin1, GPIO.OUT)              #setup pin 1 as output
GPIO.setup(pin2, GPIO.OUT)              #setup pin 2 as output

GPIO.output(pin1 , False)		#Set pin 1 to off (false)
GPIO.output(pin2 , False)		#Set pin 2 to off (false)


p1 = GPIO.PWM(pin1, frequency)
p1.start(dc)

n = True
while n:
# Checks to make sure dc is numeric, if not dc is reset back to 
# prevoius value of dc
	if str(dc).isnumeric() == True:	
		dc_old = dc
	else:
		dc = dc_old

# Asks fo a value of duty cycle, this should be a value of 0-100 inclusive
# If a text character is returned asks again for a value of 0-100

	dc = input("Enter value for PWM Duty Cycle: \nValue 0 -100 or q to quit")

# Checks dc is a numerical value

	if dc.isnumeric() == True:
		dc = int(dc)

# Checks dc is not greater than 100
		if dc  > 100:
			print ("Duty cycle must be between 0 and 100")
		else:	
# Calculated the difference between the new value of dc and the 
# previous (dc_old) value of dc
			print ("dc = "+ str(dc) + "\ndc_old = "+ str(dc_old)) 
			gap = dc-dc_old
			print ("gap = ",gap)

# If dc is greter than dc_old, i.e. LED getting brighter increse the 
# brightness in steps of 1 every 0.2 seconds
			if dc >= dc_old:
				for i in range(gap):
					dc_new = dc_old+i+1
					print ("dc_new = ",dc_new)	
					p1.ChangeDutyCycle(dc_new)
					time.sleep(0.02)

# If dc is less than dc_old, i.e. LED getting dimmer, decrease the 
# brightness in steps of 1 every 0.2 seconds
			else:
				for i in range(abs(gap)):
					dc_new = dc_old-i-1
					print ("dc_new = ",dc_new)
					p1.ChangeDutyCycle(dc_new)
					time.sleep(0.02)

# Check if dc is an alpha character, if so check for 'q' and quit
# if not q, request a number between 0 and 100.
	elif dc.isalpha() == True:
		if dc.lower() != "q": 
			print ("enter a number from 0-100 or q to quit")
		else:
			n = False		



# Cleanup GPIO pins
GPIO.cleanup()
