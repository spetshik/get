import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led =26
photo = 6
GPIO.setup(photo, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

state = 0 
while True:
    if GPIO.input(photo):
        state=0
        GPIO.output(led, state)
    else:
        state=1
        GPIO.output(led, state)
