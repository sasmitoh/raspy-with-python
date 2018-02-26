import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList =[4,17,27]

SleepTime = 0.2

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

try:
    while True:
        for i in pinList:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(SleepTime)
            GPIO.output(i, GPIO.LOW)
            time.sleep(SleepTime)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

