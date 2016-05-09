#!/usr/bin/python2
# -*- coding: utf-8 -*

from Crypto.Cipher import AES

a = ""
m = raw_input("Mode\n>>> ")
while a != "\exit":
    if m == "c":
        a = raw_input("Nom du texte\n>>> ")
        f_in = open("../_sources_txt/" + a, "r")
        f_out = open("../txt/" + a.split(".")[0] + "_e." + a.split(".")[1],
                     "wb")
        t_in = f_in.read()
        encodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC,
                           "vecteur_init_16o")
        t_in += "\0" * (16 - (len(t_in) % 16))
        texte_code = encodeur.encrypt(t_in)
        f_out.write(texte_code)
        f_out.close()
        f_in.close()
        print("Fini")

    if m == "d":
        a = raw_input("Nom du texte\n>>> ")
        f_in = open("../txt/" + a, "rb")
        t_in = f_in.read()
        decodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC,
                           "vecteur_init_16o")
        texte = decodeur.decrypt(t_in)
        while texte[-1] == "\0":
            texte = texte[:-1]
        print(texte)
        f_in.close()
