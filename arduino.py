#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
while True:
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Remplacez '/dev/ttyS1' par votre port série

    # Lire depuis l'Arduino
    data = ser.readline()
    print(data)

# Envoyer des données à l'Arduino
#ser.write(b'Hello Arduino!')

ser.close()

