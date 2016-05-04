#!/usr/bin/python2
# -*- coding: utf-8 -*

f_in_brut = open("gougenheim.txt", "r")
f_out_brut = open("dictionnaire_freq.txt", "w")

ligne = f_in_brut.readline()
while ligne != "\n" and ligne:
    f_out_brut.write(ligne.split("@")[0] + "\n")
    ligne = f_in_brut.readline()

f_in_brut.close()
f_out_brut.close()
