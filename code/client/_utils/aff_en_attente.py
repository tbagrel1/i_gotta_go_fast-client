#!/usr/bin/python2
# -*- coding: utf-8 -*

# Il faut installer la bibliothèque `cryptography` avec `pip` en tapant dans
# une invite de commande :
# >>> pip install cryptography

# Le système est un peu complexe, et fonctionne avec deux chaînes, une byte de 
# longueur voulue (`mot_de_passe`), et une autre parfaite de 16 o
# Les deux parties cryptage et décryptage doivent utiliser les mêmes deux clés

# Import des modules

import pickle
import base64
import os
from Crypto.Cipher import AES

# On ouvre le fichier
fichier = open("../score/en_attente.db", "r")
message_crypte = fichier.read()
fichier.close()

message_crypte = [elt for elt in message_crypte.split("||||||||||") if elt]
for elt in message_crypte:
    decodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")
    elt_decrypte = decodeur.decrypt(elt)
    fichier = open("temp.tmp", "w")
    fichier.write(elt_decrypte)
    fichier.close()

    fichier = open("temp.tmp", "r")
    mon_pickler = pickle.Unpickler(fichier)
    elt_decrypte_2 = mon_pickler.load()
    fichier.close()
    os.remove("temp.tmp")
    print(type(elt_decrypte_2))
    print(elt_decrypte_2)
