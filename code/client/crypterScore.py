#!/usr/bin/python2
# -*- coding: utf-8 -*

# Import des modules

import socket
import sys
import pickle
import os
import hashlib
import base64
from Crypto.Cipher import AES

def crypterScoreAttente(dico_score):

    encodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")

    checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
    liste = [checksum, dico_score]

    fichier_temp = open("score/temp.tmp", "w")
    mon_pickler = pickle.Pickler(fichier_temp)
    mon_pickler.dump(liste)
    fichier_temp.close()

    fichier_temp = open("score/temp.tmp", "r")
    texte = fichier_temp.read()
    fichier_temp.close()
    os.remove("score/temp.tmp")

    texte += "\0" * (16 - (len(texte) % 16))

    texte_crypte = base64.encodestring(encodeur.encrypt(texte))
    fichier_score_attente = open("score/en_attente.db", "a")
    fichier_score_attente.write(texte_crypte + "||||||||||")
    fichier_score_attente.close()

def envoyerScoreAttente():
    pass
#     client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_to_serv.connect(("localhost", 25565))

#     msg_recu = ""
#     while msg_recu[-4:] != "\end":
#         msg_recu += client_to_serv.recv(1024)
#     msg_recu = msg_recu[:-4]
#     print(msg_recu)

#     if msg_recu == "OK":
#         client_to_serv.send("PUSH\end")

#         msg_recu = ""
#         while msg_recu[-4:] != "\end":
#             msg_recu += client_to_serv.recv(1024)
#         msg_recu = msg_recu[:-4]
#         print(msg_recu)
#         if msg_recu == "OK":

#             # On envoie le score
#             client_to_serv.send(score + "\end")

#             msg_recu = ""
#             while msg_recu[-4:] != "\end":
#                 msg_recu += client_to_serv.recv(1024)
#             msg_recu = msg_recu[:-4]
#             print(msg_recu)

#             if msg_recu == "OK":
#                 return True

def recupererScore():
    pass
#     client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_to_serv.connect(("localhost", 25565))

#     msg_recu = ""
#     while msg_recu[-4:] != "\end":
#         msg_recu += client_to_serv.recv(1024)
#     msg_recu = msg_recu[:-4]
#     print(msg_recu)

#     if msg_recu == "OK":
#         client_to_serv.send("PULL\end")

#         msg_recu = ""
#         while msg_recu[-4:] != "\end":
#             msg_recu += client_to_serv.recv(1024)
#         msg_recu = msg_recu[:-4]
#         print(msg_recu)
#         if msg_recu == "OK":

#             msg_recu = ""
#             while msg_recu[-4:] != "\end":
#                 msg_recu += client_to_serv.recv(1024)
#             msg_recu = msg_recu[:-4]
#             print(msg_recu)

#             # msg_recu correspond à la DB récupérée
