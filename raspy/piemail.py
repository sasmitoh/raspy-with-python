import RPi.GPIO as GPIO
import time, math
import smtplib, time

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

jawab = "y"

def send_email(username, password, recipient, subject, text):
    print(username, password, recipient, subject, text)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(username, password)
    header = 'To:' + recipient + '\n' + 'From: ' + username
    header = header + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(username, recipient, msg)
    smtpserver.close()

username = "your_email@gmail.com"
password = "your_password"
recipient = "your_to_send_email@gmail.com"
subject = "project sas email"
message_a = "light 1 ON "
message_b = "light 1 OFF"
message_c = "light 2 ON "
message_d = "light 2 OFF "
message_e = "light 3 ON "
message_f = "light 3 OFF "
message_g = "lights ON all "
message_h = "lights OFF all "



while (jawab == 'y'):
    perintah = input('masukan perintah : ')
    if perintah == 'ON led1':
        GPIO.output(4,GPIO.HIGH)
        send_email(username, password, recipient, subject, message_a)
        status = 'led 1 menyala'
    elif perintah == 'OFF led1':
        GPIO.output(4,GPIO.LOW)
        send_email(username, password, recipient, subject, message_b)
        status = 'led 1 padam'
    elif perintah == 'ON led2':
        GPIO.output(17,GPIO.HIGH)
        send_email(username, password, recipient, subject, message_c)
        status = 'led 2 menyala'
    elif perintah == 'OFF led2':
        GPIO.output(17,GPIO.LOW)
        send_email(username, password, recipient, subject, message_d)
        status = 'led 2 padam'
    elif perintah == 'ON led3':
        GPIO.output(27,GPIO.HIGH)
        send_email(username, password, recipient, subject, message_e)
        status = 'led 3 menyala'
    elif perintah == 'OFF led3':
        GPIO.output(27,GPIO.LOW)
        send_email(username, password, recipient, subject, message_f)
        status = 'led 3 padam'
    elif perintah == 'ON semua':
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        send_email(username, password, recipient, subject, message_g)
        status = 'semua led menyala'
    elif perintah == 'OFF semua':
        GPIO.output(4,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        send_email(username, password, recipient, subject, message_h)
        status = 'semua led padam'
    else :
        status = 'no perintah'
    print ('status : ' + status)
    jawab = input("tambah perintah ?")
print ('terimakasih')

