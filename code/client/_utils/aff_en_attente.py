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
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Tout ce qui est dans ce bloc correspond au cryptage symétrique
# On prépare la clé Fernet qui permet de crypter et de décrypter
#------------------------------------------------------------------------------
mot_de_passe = "1234123412341234"
# cle_16o = os.urandom(16) --> Il faut que les deux parties utilisent la même
cle_16o = "1234123412341234"

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=cle_16o,
                 iterations=100000,
                 backend=default_backend())
cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
cle_fernet = Fernet(cle)
#------------------------------------------------------------------------------

# On ouvre le fichier
fichier = open("../score/en_attente.db", "rb")
message_crypte = fichier.read()
fichier.close()

for elt in message_crypte.split("||||||||||")[:-1]:
    elt_decrypte = cle_fernet.decrypt(elt)
    fichier = open("temp.tmp", "wb")
    fichier.write(elt_decrypte)
    fichier.close()

    fichier = open("temp.tmp", "rb")
    mon_pickler = pickle.Unpickler(fichier)
    elt_decrypte_2 = mon_pickler.load()
    fichier.close()
    os.remove("temp.tmp")
    print(type(elt_decrypte_2))
    print(elt_decrypte_2)
