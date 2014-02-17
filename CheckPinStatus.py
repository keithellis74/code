###########################################################
### Code to check the status of GPIO pins               ###
###                Version 00                           ###
### In this version -                                   ###
### using code from code.google.com/p/                  ###
###     raspberry-gpio-python/wiki/Outputs              ###
###########################################################

import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

print ("Pins 11 and 12 setup as outputs\nPins 13 and 14 set up as inputs")
print ("Pin 11 current status = ",GPIO.input(11))
print ("Pin 12 current status = ",GPIO.input(12))
print ("Pin 13 current status = ",GPIO.input(13))
print ("Pin 15 current status = ",GPIO.input(15))

GPIO.output(12, True)
GPIO.output(11, True)

print("Pins 11 and 12 set to HIGH")
print ("Pins 11 and 12 setup as outputs\nPins 13 and 14 set up as inputs")
print ("Pin 11 current status = ",GPIO.input(11))
print ("Pin 12 current status = ",GPIO.input(12))
print ("Pin 13 current status = ",GPIO.input(13))
print ("Pin 15 current status = ",GPIO.input(15))

###GPIO.input(chnnel) returns the status of the selected pin (channel)
### whether setup as input or an output

### GPIO.output(13), True)                      ### This returns an error as expected
### print("Try set set input 13 as HIGH")
### print ("Pins 11 and 12 setup as outputs\nPins 13 and 14 set up as inputs")
### print ("Pin 11 current status = ",GPIO.input(11))
### print ("Pin 12 current status = ",GPIO.input(12))
### print ("Pin 13 current status = ",GPIO.input(13))
###print ("Pin 15 current status = ",GPIO.input(15))

GPIO.cleanup()
