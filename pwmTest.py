import RPi.GPIO as GPIO
import time

gpio_pins = {'leftMotorPin1' : 23, 'leftMotorPin2' :7, 'rightMotorPin1':24,'rightMotorPin2':8}

GPIO.setmode(GPIO.BCM)

for number in gpio_pins:
	GPIO.setup(gpio_pins[number], GPIO.OUT)
#	number = GPIO.PWM(gpio_pins[number], 150
	print (number)

#print (leftMotorPin1)


GPIO.cleanup
