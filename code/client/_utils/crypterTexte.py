#!/usr/bin/python2
# -*- coding: utf-8 -*

import hashlib
import sys
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def crypterTexte(texte):
    # Tout ce qui est dans ce bloc correspond au cryptage symétrique
    # On prépare la clé Fernet qui permet de crypter et de décrypter
    #--------------------------------------------------------------------------
    mot_de_passe = "1234123412341234"
    cle_16o = "1234123412341234"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=cle_16o,
                     iterations=100000,
                     backend=default_backend())
    cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
    cle_fernet = Fernet(cle)
    #--------------------------------------------------------------------------
    return cle_fernet.encrypt(texte)

def decrypterTexte(texte):
    # Tout ce qui est dans ce bloc correspond au cryptage symétrique
    # On prépare la clé Fernet qui permet de crypter et de décrypter
    #--------------------------------------------------------------------------
    mot_de_passe = "1234123412341234"
    cle_16o = "1234123412341234"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=cle_16o,
                     iterations=100000,
                     backend=default_backend())
    cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
    cle_fernet = Fernet(cle)
    #--------------------------------------------------------------------------
    return cle_fernet.decrypt(texte)
