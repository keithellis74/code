###############################################
### Testing Outputs on the Raspberry Pi     ###
###            Version 01                   ###
### In this version -                       ###
### refined switching code                  ###
### veriables removed since no longer       ###
### required. Outputs always finish in off  ###
### status. Also 3 now toggles pins 11 & 12 ###
###############################################

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)                  #use pin numbers
GPIO.setup(11, GPIO.OUT)                  #setup pin 11 as output
GPIO.setup(12, GPIO.OUT)                  #setup pin 12 as output


while True:                               #This while statement works but raw_input is better

   print ("Pin11 = ", GPIO.input(11))
   print ("Pin12 = ", GPIO.input(12))
   
   input("\n\nPress 1 to toggle pin 11 or 2 to toggle pin 12:\nPress q to quit\n") # than input. Find out how to use raw_input
   if n.strip() == "1":
      GPIO.output(11, not GPIO.input(11))      

   elif n.strip() == "2":
      GPIO.output(12, not GPIO.input(12))

   elif n.strip() == "3":
      GPIO.output(11, not GPIO.input(11))
      GPIO.output(12, not GPIO.input(12))

   elif n.strip() =="q": break ### This is not working, the GPIO.cleanup() sttement is not running
   elif n.strip() =="Q": break

#GPIO.output(11, False)
#GPIO.output(12, False)
print ("Pin11 before quiting = ", GPIO.input(11))
print ("Pin12 before quiting = ", GPIO.input(12))
GPIO.cleanup()
