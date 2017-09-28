#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP_Dest = "127.0.0.1"
port = 12800

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_DGRAM = Internet
#socket.SOCK_STREAM = UDP

print 'Connexion réussi sur le serveur...'

connexion_serveur.sendto ("Hi", (IP_Dest, port))



