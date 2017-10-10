#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

latitude = 1651782 #Latitude
longitude = 8745696 #Longitude
Gite = 20
VVent = 4
DVent = 60

IP_Serv = "127.0.0.1" #Addresse du serveur
port = 12800 #Port du serveur

serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Démarage ...'
serveur.bind((IP_Serv, port))

lat3=(latitude>>24)
lat2=(latitude>>16)&0xFF
lat1=(latitude>>8)&0xFF
lat0=(latitude&0xFF)


lon3=(longitude>>24)
lon2=(longitude>>16)&0xFF
lon1=(longitude>>8)&0xFF
lon0=(longitude&0xFF)

while True:
    data, addresse = serveur.recvfrom(4)
    print 'ID: ', ord(data[0])  #Affichage de l'octet 0
    print 'Taille: ', ord(data[1]) #Affichage l'octet 1
    print 'Safran: ', ord(data[2]) #Affichage de l'octet 2
    print 'GV: ', ord(data[3]) #Affichage de l'octet 3
    print '--------------------'

    tramereponse=bytearray([data[0],data[1],VVent,DVent,lat3,lat2,lat1,lat0,lon3,lon2,lon1,lon0,Gite])
    serveur.sendto (tramereponse, (addresse)) #Envoie de la trame de reponse
