import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)

for i in range(3):
    GPIO.output(4, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(4, GPIO.LOW)
    time.sleep(0.5)
GPIO.cleanup()
