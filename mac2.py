#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OPi.GPIO as GPIO
import time

# Configuration des broches
GPIO.setboard(GPIO.PCPCPLUS)
BUTTON_PIN = 7        # Broche physique 7 (GPIO4)
COIN_ACCEPTOR_PIN = 11  # Broche physique 11 (GPIO17)

# Configuration des broches en entrée
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COIN_ACCEPTOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        coin_acceptor_state = GPIO.input(COIN_ACCEPTOR_PIN)
	print(button_state)
	print(coin_acceptor_state)
        #print(f"Bouton: {'Appuyé' if button_state else 'Relâché'} - Monnayeur: {'Pièce détectée' if coin_acceptor_state else 'Pas de pièce'}")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()

