#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

IP_Dest = "127.0.0.1" #Addresse du serveur
port = 12800 #Port du serveur
trame = bytearray([22,2,30,90])

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.AF_DGRAM = Internet
#socket.SOCK_STREAM = UDP

print 'Connexion réussi sur le serveur...'

print 'Addresse de destination: ',IP_Dest

print 'Port de destination: ',port

print 'Message envoyé: ', trame[0],trame[1],trame[2],trame[3]

connexion_serveur.sendto (trame, (IP_Dest, port)) #Envoie du message au serveur


tramereponse,addresse = connexion_serveur.recvfrom(32)


print '------------------------'

print 'Réponse du serveur:'

print 'ID: ', ord(tramereponse[0])
print 'Taille: ', ord(tramereponse[1])
print 'Vitesse du vent: ',ord(tramereponse[2]), 'Noeud'
print 'Direction du vent: ',ord(tramereponse[3]),'°'
print 'Latitude: ',ord(tramereponse[4]),ord(tramereponse[5]),ord(tramereponse[6]),ord(tramereponse[7])
print 'Longitude: ',ord(tramereponse[8]),ord(tramereponse[9]),ord(tramereponse[10]),ord(tramereponse[11])
print 'Gite: ', ord(tramereponse[12]), '°'