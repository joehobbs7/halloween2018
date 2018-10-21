import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input p$

while True: # Run forever
    if GPIO.input(18) == GPIO.HIGH:
        print("Button was pushed!")


