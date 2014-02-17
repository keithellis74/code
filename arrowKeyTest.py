#
#	arrowKeyTest.py
#
#	the purpose of this program is to control
#	the GPIO pins (or print statements) with
#	the arrow keys, using pygame
#
#	------------------------------------------

#import RPi.GPIO as GPIO
import sys, pygame
pygame.init()

size = [300, 200]

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Test")

while True:
	for event in pygame.event.get():
		if event.type ==pygame.KEYDOWN:
			if event.key ==pygame.K_UP:
				print ("up key pressed")
			elif event.key == pygame.K_RIGHT:
				print ("right key pressed")
			elif event.key == pygame.K_LEFT:
				print ("left key pressed")

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				print ("up key released")
			elif event.key == pygame.K_RIGHT:
				print ("right key released")
			elif event.key == pygame.K_LEFT:
				print ("left key released")
		

print("The End...")
pygame.QUIT
