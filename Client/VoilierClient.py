#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class VoilierClient: #Création de la classe "VoilierClient"

	def __init__(self): #Création du constructeur
		self.ipserveur="" #Stockage IP du Serveur
		self.port = 0 #Stockage Port du Serveur
		self.id = 0 #Stockage ID de la Trame
		self.gite = 0 #Stockage de la valeur de la Gite
		self.valSF = 0 #Stockage de la valeur du Safran
		self.valGV = 0 #Stockage de la valeur de la Grande voile
		self.latitude = 0 #Stockage de la Latitude
		self.longitude = 0 #Stockage de la Longitude
		self.vitVent = 0 #Stockage de la Vitesse du vent
		self.orientVent = 0 #Stockage de l'Orientation du vent


	def initCom(self, ip, port): #Création de la méthode 'initCom'
		self.ipserveur = ip #Récupération de l'adresse IP et stockage dans 'self.ipserveur'
		self.port = port #Récupération dun Port et stockage dans 'self.port'
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#socket.AF_DGRAM = Internet
		#socket.SOCK_STREAM = UDP


	def txrx(self, valSF, valGV): #Création de la méthode 'txrx'

			self.valSF = valSF
			self.valGV = valGV
			
			trame = bytearray([self.id,2,self.valSF,self.valGV]) #Définition de la Trame d'envoie au serveur

			print 'Message envoyé: ', trame[0],trame[1],trame[2],trame[3] #Affichage de la Trame envoyé

			self.socket.sendto (trame, (self.ipserveur, self.port)) #Envoie du message au serveur

			tramereponse,addresse = self.socket.recvfrom(32) #Réception des données depuis le serveur

			#/ Latitude \#
			lat3=ord(tramereponse[4]) #Récupération valeur de 'lat3'
			lat2=ord(tramereponse[5]) #Récupération valeur de 'lat2'
			lat1=ord(tramereponse[6]) #Récupération valeur de 'lat1'
			lat0=ord(tramereponse[7]) #Récupération valeur de 'lat0'

			latitude = lat3<<24|lat2<<16|lat1<<8|lat0 #Décalage des bits

			if lat3 > 127:                             #                         
				latitude=(~latitude)&0xFFFFFFFF        #
				latitude=latitude+1                    # Permet de mettre la latitude en valeur négatif
				latitude=latitude*-1                   #
			#/ Latitude \#

			#/ Longitude \#
			lon3=ord(tramereponse[8]) #Récupération valeur de 'lon3'
			lon2=ord(tramereponse[9]) #Récupération valeur de 'lon2'
			lon1=ord(tramereponse[10]) #Récupération valeur de 'lon1'
			lon0=ord(tramereponse[11]) #Récupération valeur de 'lon0'

			longitude = lon3<<24|lon2<<16|lon1<<8|lon0 #Décalage des bits

			if lon3 > 127:                             #
				longitude=(~longitude)&0xFFFFFFFF      #
				longitude=longitude+1                  # Permet de mettre la longitude en valeur négatif
				longitude=longitude*-1                 #
			#/ Longitude \#

			self.latitude = float(latitude) / 1000000 #Division du résultat de 'latitude' par '1000000'
			self.longitude = float(longitude) / 1000000 #Division du résultat de 'longitude' par '1000000'
			self.gite = ord(tramereponse[12])#Récupération de la Trame de réponse et stockage dans 'self.gite'
			self.vitVent = ord(tramereponse[2])#Récupération de la Trame de réponse et stockage dans 'self.vitvent'
			self.orientVent = ord(tramereponse[3])#Récupération de la Trame de réponse et stockage dans 'self.orientvent'
			self.id = ord(tramereponse[0])#Récupération de la Trame de réponse et stockage dans 'self.id'
			self.taille = ord(tramereponse[1]) #Récupération de la Trame de réponse et stockage dans 'self.taille'
			self.id+=1 #Incrémente de 1 l'ID




client = VoilierClient()
#client.initCom("127.0.0.1",12800) #Connexion au serveur avec l'IP et le Port
#client.valSF=10 #On définit une valeur pour le Safran
#client.valGV=48 #On définit une valeur pour la Grande voile
#client.txrx()
#print '------------------------------------'
#print 'Paramètre du serveur:'
#print 'Adresse IP: ',client.ipserveur #Affichage de l'adresse IP contenu dans 'self.ipserveur'
#print 'Port du serveur: ',client.port #Affichage du port du serveur contenu dans 'self.port'
#print '------------------------------------'
#print 'ID: ', client.id #Affichage dde l'ID contenu dans 'self.id'
#print 'Taille: ',client.taille #Affichage de la taille contenu dans 'self.taille'
#print 'Gite: ',client.gite #Affichage de la gite contenu dans 'self.gite'
#print 'Latitude: ',client.latitude #Affichage de la latitude contenu dans 'self.latitude'
#print 'Longitude: ',client.longitude #Affichage de la longitude contenu dans 'self.longitude'
#print 'Vitesse du vent: ',client.vitVent,' Noeud' #Affichage de la vitesse du vent contenu dans 'self.vitVent'
#print 'Orientation du vent: ',client.orientVent #Affichage de l'orientation du vent contenu dans 'self.orientVent'
#print 'Valeur Safran: ',client.valSF #Affichage de la valeur du safran contenu dans 'self.valSF'
#print 'Valeur Grande Voile: ',client.valGV #Affichage de la valeur de la grande voile contenu dans 'self.valGV'