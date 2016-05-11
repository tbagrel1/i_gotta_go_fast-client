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
    try:
        client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_to_serv.connect(("bagrel.ddns.net", 25565))
        co_ok = True
    except:
        co_ok = False
    if not co_ok:
        try:
            client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_to_serv.connect(("pi-pc", 25565))
            co_ok = True
        except:
            co_ok = False
    if co_ok:
        fichier_score = open("score/en_attente.db", "r")
        scores_a_envoyer = fichier_score.read()
        print(scores_a_envoyer)
        fichier_score.close()

envoyerScoreAttente()
