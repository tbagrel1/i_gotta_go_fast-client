#!/usr/bin/python2
# -*- coding: utf-8 -*
#ref_to_md

from Crypto.Cipher import AES
import binascii

def crypterTexte(texte):
    encodeur = AES.new("mot_de_passe_16o", AES.MODE_CBC, "vecteur_init_16o")
    texte += "\0" * (16 - (len(texte) % 16))
    texte_code = encodeur.encrypt(texte)
    return binascii.b2a_hex(texte_code)

def decrypterTexte(texte_code):
    decodeur = AES.new("mot_de_passe_16o", AES.MODE_CBC, "vecteur_init_16o")
    texte = decodeur.decrypt(binascii.a2b_hex(texte_code))
    while texte[-1] == "\0":
        texte = texte[:-1]
    return texte
