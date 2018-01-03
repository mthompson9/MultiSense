import RPi.GPIO as GPIO

import time

from firebase import firebase

import requests


firebase_url = 'https://multisensor9.firebaseio.com'
timestamp = time.strftime("%Y_%m_%d" + "@ " + "%H:%M%S")
userName = ''
userPass = ''
reading = 0

GPIO.setwarnings(False)



TRIG = 23

ECHO = 24

def distChecker ():
    
    for i in range (1, 10):

##    print ("Distance Measurement In Progress")
    
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(TRIG,GPIO.OUT)

        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIG, False)

##    print ("Waiting For Sensor To Settle")

        time.sleep(2)

        GPIO.output(TRIG, True)

        time.sleep(0.00001)

        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:

          pulse_start = time.time()
    
        while GPIO.input(ECHO)==1:

          pulse_end = time.time()
  
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration*17150

        distance = round(distance, 2)
        
        result = ("Distance: " , distance , " cm")

        GPIO.cleanup()
        
        return result
    
while True:
    print (distChecker())
  