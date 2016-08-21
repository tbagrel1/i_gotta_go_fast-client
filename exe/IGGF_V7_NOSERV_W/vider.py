#!/usr/bin/python2
# -*- coding: utf-8 -*

import pickle

fichier = open("score/local_db.db", "rb")
mon_pickler = pickle.Unpickler(fichier)
liste = mon_pickler.load()
fichier.close()

liste2 = []
for elt in liste:
    if str(elt["pseudo"])[0] == "#":
        liste2.append(elt)

fichier = open("score/local_db.db", "wb")
mon_pickler = pickle.Pickler(fichier)
mon_pickler.dump(liste2)
fichier.close()
