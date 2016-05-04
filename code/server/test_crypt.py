#!/usr/bin/python2
# -*- coding: utf-8 -*

# Il faut installer la bibliothèque `cryptography` avec `pip` en tapant dans
# une invite de commande :
# >>> pip install cryptography

# Le système est un peu complexe, et fonctionne avec deux chaînes, une byte de 
# longueur voulue (`mot_de_passe`), et une autre parfaite de 16 o
# Les deux parties cryptage et décryptage doivent utiliser les mêmes deux clés

# Import des modules

import base64
# import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Tout ce qui est dans ce bloc correspond au cryptage symétrique
# On prépare la clé Fernet qui permet de crypter et de décrypter
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

# On crypte et on affiche
message_crypte = cle_fernet.encrypt("Ceci est le message secret")
print(message_crypte)
print("------------")

# On enregistre dans le fichier
fichier = open("message_crypte.txt", "w")
fichier.write(message_crypte)
fichier.close()
