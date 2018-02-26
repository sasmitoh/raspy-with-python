import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

jawab = "y"

while (jawab == 'y'):
    perintah = input('masukan perintah : ')
    if perintah == 'ON led1':
        GPIO.output(4,GPIO.HIGH)
        status = 'led 1 menyala'
    elif perintah == 'OFF led1':
        GPIO.output(4,GPIO.LOW)
        status = 'led 1 padam'
    elif perintah == 'ON led2':
        GPIO.output(17,GPIO.HIGH)
        status = 'led 2 menyala'
    elif perintah == 'OFF led2':
        GPIO.output(17,GPIO.LOW)
        status = 'led 2 padam'
    elif perintah == 'ON led3':
        GPIO.output(27,GPIO.HIGH)
        status = 'led 3 menyala'
    elif perintah == 'OFF led3':
        GPIO.output(27,GPIO.LOW)
        status = 'led 3 padam'
    elif perintah == 'ON semua':
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        status = 'semua led menyala'
    elif perintah == 'OFF semua':
        GPIO.output(4,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        status = 'semua led padam'
    else :
        status = 'no perintah'
    print ('status : ' + status)
    jawab = input("tambah perintah ?")
print ('terimakasih')

