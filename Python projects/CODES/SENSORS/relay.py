import RPi.GPIO as GPIO      
import time
import os
os.system("sudo pigpiod")

relayPin = 20

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin, GPIO.HIGH)


while True :
    GPIO.output(relayPin, GPIO.LOW)
    time.sleep(3)
    GPIO.output(relayPin, GPIO.HIGH)
    time.sleep(3)
