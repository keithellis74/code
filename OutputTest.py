###############################################
### Testing Outputs on the Raspberry Pi     ###
###            Version 00                   ###
### In this version -                       ###
### sets up GPIO with board pin numbers     ###
### Switches two pins high/low with         ###
### kayboard input                          ###
###############################################

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)                  #use pin numbers
GPIO.setup(11, GPIO.OUT)                  #setup pin 11 as output
GPIO.setup(12, GPIO.OUT)                  #setup pin 12 as output


Pin11 = -1                                # Variable used to switch pin value
Pin11Value = 0                            # Variable to set value of pin
Pin12 = -1                                # Variable used to switch pin value
Pin12Value = 0                            # Variable to set value of pin

while True:                               #This while statement works but raw_input is better
   print ("\nPin11Value = ", Pin11Value)   
   print ("Pin11 = ",Pin11)
   print ("Pin12Value = ", Pin12Value)
   print ("Pin12 = ",Pin12)
   
   n=input("\n\nPress 1 to toggle pin 11 or 2 to toggle pin 12:\nPress q to quit\n") # than input. Find out how to use raw_input
   if n.strip() == "1":
      Pin11 *= -1
      if Pin11 == -1:
         Pin11Value = 0
      else:
         Pin11Value = 1
      GPIO.output(11, Pin11Value)
      

   elif n.strip() == "2":
      Pin12 *=-1
      if Pin12 == -1:
         Pin12Value = 0
      else:
         Pin12Value = 1
      GPIO.output(12, Pin12Value)

   elif n.strip() =="q": break 
   elif n.strip() =="Q": break

GPIO.cleanup()

