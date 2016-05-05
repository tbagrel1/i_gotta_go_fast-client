# -*- coding: utf-8 -*
#..Les Modules:
#.Import du module socket afin de communiquer avec le clien 
#.qui lui envera des informations sur les scores.
import socket
#.Import du modules pickle qui permet de recuperer ou 
#.encoder sous forme chiffré brut une ligne de code ici en 
#.l'ocurence on "pickle" les données du joueur qui son créé 
#.sous forme de de liste impossible a recupere en l'etat, 
#.c'est pourquoi on la transfor en "chiffré" signalant que 
#.c'est un liste que l'on recupere.
import pickle

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#..Les fonctions:
#.On recupere une ligne "pickle" correspondant au score, la 
#.fonctions permet de rendre lisible les données que l'on 
#.recupere sous forme texte et les passer sous forme python
def unpick(msg):
	doc_pick = open("pickle.txt", "wb")
	doc_pick.write(msg)
	a = pickle.load(open("pickle.txt", "rb"))
	doc_pick.close()
	return a

mot_de_passe = "                "
cle_16o = "                "
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=cle_16o,
                 iterations=100000,
                 backend=default_backend())

cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
cle_fernet = Fernet(cle)

serv_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_co.bind(('',12345))
serv_co.listen(1)
while True:
	serv_to_client, infos_co = serv_co.accept()
	print(infos_co)
	msg_recu = ""
	while msg_recu[-4:] != "\end":	
		msg_recu += serv_to_client.recv(1024)
	print(msg_recu)
	msg_recu = msg_recu[:-4]
	
	fichier = open("message_crypte.txt", "wb")
	fichier.write(msg_recu)
	fichier.close()
	
	fichier = open("message_crypte.txt", "rb")
	msg_crypte = fichier.read()
	fichier.close()
	msg_decrypte = cle_fernet.decrypt(msg_crypte)
	msg_recu_final = unpick(msg_decrypte)

	serv_to_client.send("Ok !\end")
	serv_to_client.close()

