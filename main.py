import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import pygame.mixer as mixer # Import PyGame Mixer Library
import random

mixer.init()

def button_callback(channel):
    a = random.randint(1,5)
    print("Button was pushed!\n\tRandom choice is " + str(a))
    if a==1:
        mixer.music.load('laugh.mp3')
    elif a==2:
	mixer.music.load('chains.mp3')
    elif a==3:
	mixer.music.load('thunder.mp3')
    elif a==4:
	mixer.music.load('scream.mp3')
    elif a==5:
	mixer.music.load('siren.mp3')
    mixer.music.play()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input p$

GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback,bouncetime=2000) # Setup event on pin 10 rising edge
message = input('Press enter to exit\n\n') # Run until someone presses enter
print(message)
GPIO.cleanup() # Clean up
mixer.quit()
