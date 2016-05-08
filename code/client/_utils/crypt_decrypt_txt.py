#!/usr/bin/python2
# -*- coding: utf-8 -*


import crypterTexte

a = ""
m = raw_input("Mode\n>>> ")
while a != "\exit":
    if m == "c":
        a = raw_input("Nom du texte\n>>> ")
        f_in = open("../_sources_txt/" + a, "r")
        f_out = open("../txt/" + a.split(".")[0] + "_e." + a.split(".")[1],
                     "w")
        t_in = f_in.read()
        f_out.write(crypterTexte.crypterTexte(t_in))
        f_out.close()
        f_in.close()
        print("Fini")

    if m == "d":
        a = raw_input("Nom du texte\n>>> ")
        f_in = open("../txt/" + a, "r")
        t_in = f_in.read()
        print(crypterTexte.decrypterTexte(t_in))
