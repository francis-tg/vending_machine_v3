#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
from time import sleep
import sys, requests, socket, json

count = 0

# Configuration du port série
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adapter '/dev/ttyUSB0' au port série utilisé par votre Arduino Mega

def send_post_request(url, json_data):
    try:
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(json_data), headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Échec de l'envoi de la requête POST. Code d'état : %s" % response.status_code)
    except requests.RequestException as e:
        print("Une erreur s'est produite : %s" % e)
    return None

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.error as e:
        print("Une erreur s'est produite : %s" % e)
    return None

def detecter_piece(channel):
    global count
    count += 100
    print("Pièce détectée ! Montant total : " + str(count))

def detectBtnPush(channel):
    global count
    #send_post_request(url="http://" + get_local_ip() + ":4000/api/tickets/buy", json_data={"price": count})
    count = 0

try:
    print("Appuyez sur CTRL+C pour quitter")
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        if line == 'button_pressed':
           detectBtnPush(None)
        elif 'credit:'in line:
	   print(line)
           detecter_piece(None)

except KeyboardInterrupt:
    ser.close()
    print("Au revoir.")

