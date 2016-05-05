#!/usr/bin/python2
# -*- coding: utf-8 -*

#.##Modules :
#.Import du module socket afin de communiquer avec le client qui lui envera 
#.des informations sur les scores.
import socket
#.Import du modules pickle qui permet de recuperer un objet python stocké dans 
#.un fichier texte
import pickle
#.Import des modules pour la cryptographie
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#.##Format de données reçues par le serveur
#.On reçoit du client plusieurs chaînes de caractères correspondant à une 
#.liste contenant le code de la fonction de cryptage, la checksum du fichier 
#.qui appelle la fonction ainsi que le dictionnaire de score, le tout crypté

#.##Les fonctions :
#.On recupere une ligne "pickle" correspondant au score, la
#.fonctions permet de rendre lisible les données que l'on
#.recupere sous forme texte et les passer sous forme python


def unpick(msg):
<<<<<<< HEAD
    doc_pick = open("pickle.txt", "wb")
    doc_pick.write(msg)
    return pickle.load(open("pickle.txt", "rb"))
=======
	doc_pick = open("pickle.txt", "wb")
	doc_pick.write(msg)
	a = pickle.load(open("pickle.txt", "rb"))
	doc_pick.close()
	return a
>>>>>>> 2d016ac338601856caa3cbf005e2b40cb82ba18d

#.Tout ce qui est dans ce bloc correspond au cryptage symétrique
#.On prépare la clé Fernet qui permet de crypter et de décrypter
#------------------------------------------------------------------------------
mot_de_passe = "                "
# cle_16o = os.urandom(16) --> Il faut que les deux parties utilisent la même
cle_16o = "                "

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=cle_16o,
                 iterations=100000,
                 backend=default_backend())
cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
cle_fernet = Fernet(cle)
#------------------------------------------------------------------------------

#.On lance le service de connection
serv_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#.On utilise le port `25565`
serv_co.bind(('', 25565))
#. On écoute un maximum d'une connection à la fois
serv_co.listen(1)

#.Tant que le serveur est en marche
while True:
    #.On accepte une connection et on récupère les informations de connection
    (serv_to_client, infos_co) = serv_co.accept()
    #.On affiche les informations de connection
    print(infos_co)
    #.On envoi un message au client pour dire qu'il est bien connecté
    serv_to_client.send("OK\end")

    msg_recu = ""
    #.Tant que le message n'est pas arrivé complétement
    while msg_recu[-4:] != "\end":
        #.On accepte les données (on vide le buffer)
        msg_recu += serv_to_client.recv(1024)
    #.On supprime le `\end` à la fin
    msg_recu = msg_recu[:-4]
    #.On affiche le message reçu
    print(msg_recu)
    #.On envoi un message au client pour dire que le score est bien arrivé
    serv_to_client.send("OK\end")
    serv_to_client.close()

    # fichier = open("message_crypte.txt", "wb")
    # fichier.write(msg_recu)
    # fichier.close()

    # fichier = open("message_crypte.txt", "rb")
    # msg_crypte = fichier.read()
    # fichier.close()
    # msg_decrypte = cle_fernet.decrypt(msg_crypte)
    # msg_recu_final = unpick(msg_decrypte)

    # serv_to_client.send("Ok !\end")
    # serv_to_client.close()
