#!/usr/bin/python2
# -*- coding: utf-8 -*-

#.#Projet ISN - Fast Writing
#.**Auteurs :  **  Thomas BAGREL, Julien ROMARY  
#.**Version :  **  V1.0.0 - Test  
#.**Date :     **  03.03.2016  

#.##Import des modules
#.On importe `os.system` pour utiliser des commandes systèmes, et
#.`sys.argv` pour utiliser les arguments passés au programme lors du
#.lancement
from os import system
from sys import argv

#.##Déclaration des fonctions
#.###Fonction permettant de tester la parité d'un nombre
#.Renvoie `True` si le paramètre `nombre` est pair, et `False` sinon
def est_pair(nombre):
    # On regarde le modulo du nombre par 2 :
    if nombre % 2 == 0:
        return True
    else:
        return False

#.##Corps du programme
#.On demande à l'utilisateur de saisir un nombre `a`
a = input(">>> ")

#.On affiche si le nombre est _pair_ ou _impair_
print(est_pair(a))

#.On utilise les modules importés
system("echo \"{}\"".format(argv[0]))
