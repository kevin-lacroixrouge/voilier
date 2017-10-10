#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP_Serv = "192.168.2.254" #Addresse du serveur
port = 12800 #Port du serveur

serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Démarage ...'
serveur.bind((IP_Serv, port))

while True:
    data, addresse = serveur.recvfrom(6)
    print 'Donner reçu: ', data #Affichage des données reçu


