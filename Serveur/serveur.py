#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP_Serv = "127.0.0.1"
port = 12800

serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Démarage ...'
serveur.bind((IP_Serv, port))

while True:
    data, addresse = serveur.recvfrom(6)
    print 'Donner reçu: ', data


