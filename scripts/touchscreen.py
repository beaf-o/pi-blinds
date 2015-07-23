
import pygame
import time
import RPi.GPIO as GPIO
from pygame.locals import *
import glob
import sys
import os

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

#setup gpio
#GPIO.setmode(GPIO.BCM)
#GPIO.setup( 4, GPIO.OUT)
#GPIO.setup( 5, GPIO.OUT)
#GPIO.setup( 6, GPIO.OUT)
#GPIO.setup(12, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)

#enable pull-up resistors
#GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#define some colors
#color    R    G    B
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)
black = (  0,   0,   0)
cyan  = (  0, 255, 255)

#initial state colors for indicators
state_color1 = red
state_color2 = red
state_color3 = red
state_color4 = red
state_color5 = red
state_color6 = red
state_color7 = red
state_color8 = red
state_color9 = red
state_color10 = red

pygame.init()

#screen size
width = 320
height = 240
size = (width, height)
screen = pygame.display.set_mode(size)

#define font
font = pygame.font.Font(None, 20)

#initial output state
gpio_state4  = False
gpio_state5  = False
gpio_state6  = False
gpio_state12 = False
gpio_state13 = False


running = True

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        #GPIO.cleanup()        
                        running = 0
                
                if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                         
                #if touchscreen pressed
	        if event.type == pygame.MOUSEBUTTONDOWN:
			#get position
        	        pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                	
			#print "touched"
			#print pos

        	        #check in which area (button) the touchscreen was touched
                        #each area/button = 55x55px
			if 5 <= pos[0] <= 60 and 5 <= pos[1] <= 60:
                        	gpio_state4 = not gpio_state4
                        	if gpio_state4 == True:
                                	#GPIO.output(4, GPIO.HIGH)
                                	state_color1 = green
                                	time.sleep(0.2)

                        	else:
                                	#GPIO.output(4, GPIO.LOW)
                                	state_color1 = red
                                	time.sleep(0.2)

                	if 65 <= pos[0] <= 120 and 5 <= pos[1] <= 60:
                        	gpio_state5 = not gpio_state5
                        	if gpio_state5 == True:
                                	#GPIO.output(5, GPIO.HIGH)
                                	state_color2 = green
                                	time.sleep(0.2)

                        	else:
                                	#GPIO.output(5, GPIO.LOW)
                                	state_color2 = red
                                	time.sleep(0.2)

                	if 125 <= pos[0] <= 180 and 5 <= pos[1] <= 60:
                        	gpio_state6 = not gpio_state6
                        	if gpio_state6 == True:
                                	#GPIO.output(6, GPIO.HIGH)
                                	state_color3 = green
                                	time.sleep(0.2)

                        	else:
                                	#GPIO.output(6, GPIO.LOW)
                                	state_color3 = red
                                	time.sleep(0.2)

                	if 185 <= pos[0] <= 240 and 5 <= pos[1] <= 60:
                        	gpio_state12 = not gpio_state12
                        	if gpio_state12 == True:
                                	#GPIO.output(12, GPIO.HIGH)
                                	state_color4 = green
                                	time.sleep(0.2)

                        	else:
                                	#GPIO.output(12, GPIO.LOW)
                                	state_color4 = red
                                	time.sleep(0.2)

                	if 245 <= pos[0] <= 300 and 5 <= pos[1] <= 60:
                        	gpio_state13 = not gpio_state13
                        	if gpio_state13 == True:
                                	#GPIO.output(13, GPIO.HIGH)
                                	state_color5 = green
                                	time.sleep(0.2)

                        	else:
                                	#GPIO.output(13, GPIO.LOW)
                                	state_color5 = red
                                	time.sleep(0.2)

                        
        #change indicator's color if input changes (LOW = red, HIGH = green)
        #if GPIO.input(16) == 1:
        #        state_color6 = green
        #else:
        #        state_color6 = red#

        #if GPIO.input(19) == 1:
        #        state_color7 = green
        #else:
        #        state_color7 = red


        #if GPIO.input(20) == 1:
        #        state_color8 = green
        #else:
        #        state_color8 = red

        #if GPIO.input(21) == 1:
        #        state_color9 = green
        #else:
        #        state_color9 = red

        #if GPIO.input(26) == 1:                        
        #        state_color10 = green
        #else:
        #        state_color10 = red
                        
        #lets draw some buttons and indicators        
        pygame.draw.rect(screen, cyan , (  5,   5,  55,  25))
        pygame.draw.rect(screen, cyan , ( 65,   5,  55,  25))
        pygame.draw.rect(screen, cyan , (125,   5,  55,  25))
        pygame.draw.rect(screen, cyan , (185,   5,  55,  25))
        pygame.draw.rect(screen, cyan , (245,   5,  55,  25))

        pygame.draw.rect(screen, cyan , (  5,   75,  55,  25))
        pygame.draw.rect(screen, cyan , ( 65,   75,  55,  25))
        pygame.draw.rect(screen, cyan , (125,   75,  55,  25))
        pygame.draw.rect(screen, cyan , (185,   75,  55,  25))
        pygame.draw.rect(screen, cyan , (245,   75,  55,  25))
        
        pygame.draw.rect(screen, state_color1 , (  5,   30,  55,  25))
        pygame.draw.rect(screen, state_color2 , ( 65,   30,  55,  25))
        pygame.draw.rect(screen, state_color3 , (125,   30,  55,  25))
        pygame.draw.rect(screen, state_color4 , (185,   30,  55,  25))
        pygame.draw.rect(screen, state_color5 , (245,   30,  55,  25))

        pygame.draw.rect(screen, state_color6 , (  5,   100,  55,  25))
        pygame.draw.rect(screen, state_color7 , ( 65,   100,  55,  25))
        pygame.draw.rect(screen, state_color8 , (125,   100,  55,  25))
        pygame.draw.rect(screen, state_color9 , (185,   100,  55,  25))
        pygame.draw.rect(screen, state_color10 , (245,   100,  55,  25))

        #create some labels for buttons
        label1 = font.render ("OUT 4", 1, black)
        label2 = font.render ("OUT 5", 1, black)
        label3 = font.render ("OUT 6", 1, black)
        label4 = font.render ("OUT 12", 1, black)
        label5 = font.render ("OUT 13", 1, black)

        label6 = font.render ("IN 16", 1, black)
        label7 = font.render ("IN 19", 1, black)
        label8 = font.render ("IN 20", 1, black)
        label9 = font.render ("IN 21", 1, black)
        label10 = font.render ("IN 26", 1, black)

        #display labels
        screen.blit(label1, (  5,   5))
        screen.blit(label2, ( 65,   5))
        screen.blit(label3, (125,   5))
        screen.blit(label4, (185,   5))
        screen.blit(label5, (245,   5))

        screen.blit(label6, (  5,  75))
        screen.blit(label7, ( 65,  75))
        screen.blit(label8, (125,  75))
        screen.blit(label9, (185,  75))
        screen.blit(label10, (245,  75))                        
        #refresh screen        
        pygame.display.update()
        time.sleep(0.01)

