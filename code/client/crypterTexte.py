#!/usr/bin/python2
# -*- coding: utf-8 -*

from Crypto.Cipher import AES

def crypterTexte(texte):
    encodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")
    texte += "\0" * (16 - (len(texte) % 16))
    texte_code = encodeur.encrypt(texte)
    return texte_code

def decrypterTexte(texte_code):
    decodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")
    texte = decodeur.decrypt(texte_code)
    while texte[-1] == "\0":
        texte = texte[:-1]
    return texte
