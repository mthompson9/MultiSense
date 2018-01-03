import RPi.GPIO as GPIO

import time

import json

from firebase import firebase

import requests

firebase = firebase.FirebaseApplication('https://multisensor9.firebaseio.com/')
firebase_url = 'https://multisensor9.firebaseio.com'
timestamp = time.strftime("%Y_%m_%d" + "@ " + "%H:%M%S")
userName = str('')
userPass = str('')
reading = 0
TRIG = 23
ECHO = 24

GPIO.setwarnings(False)

def chooseSensorType (type) :
    options = ['Temperature', 'Light', 'Height', 'Humidity', 'Moisture']
    sensorType = options[type]
    return sensorType



def dbDataPush(pushThis, ID, user, measure ) :
    try:
      result = requests.post(firebase_url + '/' + 'Readings/' + str(user) + '/' + str(ID) + '/' + str(measure) + '.json' + '/', data=json.dumps(pushThis))
      return result
    except Exception as a:
        print('There was an error')
        return

def distChecker ():
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
        
        result = (distance)

        GPIO.cleanup()
        
        print ("Distance: " , distance , " cm")
        
        return result


def fakePis () :
    userName = raw_input('What is your name: ')
    userPass = raw_input('Password please: ')
    Pi = raw_input('Which Pi is this: ')
    sType = chooseSensorType(2)
    PiId = 'pi_' + (Pi)
    myPass = 'password'
    while True:
        data = (distChecker())
        dbDataPush(data, PiId, userName, sType)
        

while True:
    fakePis()
  
