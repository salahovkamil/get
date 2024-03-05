import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
while True:
    GPIO.output(21, GPIO.input(24))

