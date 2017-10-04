#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP_Dest = "192.168.0.222" #Addresse du serveur
port = 12800 #Addresse du serveur

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_DGRAM = Internet
#socket.SOCK_STREAM = UDP

print 'Connexion réussi sur le serveur...'

connexion_serveur.sendto ("Hi", (IP_Dest, port))

print 'Message envoyé'


