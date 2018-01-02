import math
import time
import os
import glob
import time
import requests
import random
from random import randint
import json
from firebase import firebase
from firebase import firebase_token_generator



#Declarations
firebase = firebase.FirebaseApplication('https://multisensor9.firebaseio.com/')
firebase_url = 'https://multisensor9.firebaseio.com'
timestamp = time.strftime("%Y_%m_%d" + "@ " + "%H:%M%S")
userName = ''
userPass = ''
reading = 0


def chooseSensorType (type) :
    options = ['Temperature', 'Light', 'Height', 'Humidity', 'Moisture']
    sensorType = options[type]
    return sensorType



def dbDataPush(pushThis, ID, user, measure ) :
    try:
      result = requests.post(firebase_url + '/' + 'Readings/' + user + '/' + ID + '/' + measure + '.json' + '/', data=json.dumps(pushThis))
      return result
    except Exception as a:
        print('There was an error')
        return



def fakePis () :
    userName = input('What is your name: ')
    userPass = input('Password please: ')
    for x in range (0, 10) :
        Pi = randint(0, 4)
        snsr = randint(0,4)
        sType = chooseSensorType(snsr)
        PiId = 'pi' + str(Pi)
        myPass = 'password'
        data = (randFloats(1, PiId, userName, randint(0,4)))
        dbDataPush(data, PiId, userName, sType)
        print('Readings have been Pushed to node ' + userName)
    print('process completed successfully')




def randFloats (iter, ID, Usr, snsr) :
    for iter in range (0, iter) :
        reading = random.uniform(0, 100)

        data = {'UserID':Usr, 'Sensor ID':snsr, 'Sensor Type':chooseSensorType(snsr), 'Reading':reading, 'Time':timestamp}
    return (data);

print('Starting now')
fakePis()
















