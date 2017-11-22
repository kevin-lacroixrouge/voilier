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

tramereponse,addresse = connexion_serveur.recvfrom(32) #Reçoit les données depuis le serveur

#latitude = (ord(tramereponse[4])<<24)+(ord(tramereponse[5])<<16)+(ord(tramereponse[6])<<8)+(ord(tramereponse[7])) #Décalage des bits
lat3=ord(tramereponse[4])
lat2=ord(tramereponse[5])
lat1=ord(tramereponse[6])
lat0=ord(tramereponse[7])

latitude = lat3<<24|lat2<<16|lat1<<8|lat0

if lat3 > 127:
	latitude=(~latitude)&0xFFFFFFFF
	latitude=latitude+1
	latitude=latitude*-1

#longitude = (ord(tramereponse[8])<<24)+(ord(tramereponse[9])<<16)+(ord(tramereponse[10])<<8)+(ord(tramereponse[11])) #Décalage des bits
lon3=ord(tramereponse[8])
lon2=ord(tramereponse[9])
lon1=ord(tramereponse[10])
lon0=ord(tramereponse[11])

longitude = lon3<<24|lon2<<16|lon1<<8|lon0

if lon3 > 127:
	longitude=(~longitude)&0xFFFFFFFF
	longitude=longitude+1
	longitude=longitude*-1


print '------------------------'

print 'Réponse du serveur:'

print 'ID: ', ord(tramereponse[0])
print 'Taille: ', ord(tramereponse[1])
print 'Vitesse du vent: ',ord(tramereponse[2]), 'Noeud'
print 'Direction du vent: ',ord(tramereponse[3]),'°'
print 'Latitude: ', float(latitude) / 1000000
#print 'Latitude: ', float(lat3+lat2+lat1+lat0) / 1000000
print 'Longitude: ',float(longitude) / 1000000
#print 'Longitude: ',float(lon3+lon2+lon1+lon0) / 1000000
print 'Gite: ', ord(tramereponse[12]),'°'

