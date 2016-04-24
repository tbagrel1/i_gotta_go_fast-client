#!/usr/bin/python2
# -*- coding: utf-8 -*

#ref_to_md

#.#Import des modules

#.Import de `__future__.division` pour la division décimale même sur les `int`
from __future__ import division

#.Import des bibliothèques standards de `python`
from time import time, sleep
import sys
#.Import de la biblothèque `re` pour l'utilisation d'expressions régulières
import re
#.Import de la bibliothèque `atexit` nécessaire pour la création du `.exe`
import atexit

#.#Import des 3 modules pythons : `FenetreBVN`, `Menu` et `Module`
import fenetrebvn
import menu
import module

#.#Programme principal

#.##Fonction `main`
#.Fonction ne prenant pas d'arguments et permettant de lancer le programme
def main():
    #.On appelle la fonction principale `main` de `FenetreBVN`
    quitter = fenetrebvn.main()
    if quitter:
        return

    while True:
        #.On appelle la fonction principale `main` de `Menu`
        param = menu.main()
        if not param:
            return
        #.On appelle la fonction principale `main` de `Module` en lui passant 
        #.les paramètres saisis dans le menu
        module.main(param)

#.##Test de lancement standalone
#.Test permettant de lancer le programme si il est exécuté directement tout 
#.seul, sans import
if __name__ == "__main__":
    #.On appelle la fonction `main` définit plus haut
    main()
