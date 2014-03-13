#!/usr/bin/env python3
 
# Load library functions we want
import time
import os
import sys
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)

 
# Re-direct our output to standard error, we need to ignore standard out to hide some nasty print statements from pygame
sys.stdout = sys.stderr
 
 
 
# Setup pygame
os.environ["SDL_VIDEODRIVER"] = "dummy" # Removes the need to have a GUI window
pygame.init()

while True:
        for event in pygame.event.get():
                if event.type ==pygame.KEYDOWN:
                        if event.key ==pygame.K_UP:
				GPIO.output(23,True)
                                print ("up key pressed")
                        elif event.key == pygame.K_RIGHT:
                                print ("right key pressed")
                        elif event.key == pygame.K_LEFT:
                                print ("left key pressed")

                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
				GPIO.output(23,False)
                                print ("up key released")
                        elif event.key == pygame.K_RIGHT:
                                print ("right key released")
                        elif event.key == pygame.K_LEFT:
                                print ("left key released")


print("The End...")
pygame.QUIT
