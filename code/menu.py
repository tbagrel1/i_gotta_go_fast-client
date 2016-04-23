#!/usr/bin/python2
# -*- coding: utf-8 -*-
#ref_to_md

#.#Import des modules

#.Import de `__future__.division` pour la division décimale même sur les `int`
from __future__ import division
#.Import des bibliothèques pour `PyQt` (interface graphique)
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#.Import de la fenêtre graphique designée avec *Qt Creator*
from ui_menu import Ui_Menu
#.Import des bibliothèques standards de `python`
from time import time, sleep
import sys
#.Import de la biblothèque `re` pour l'utilisation d'expressions régulières
import re
#.Import de la bibliothèque `atexit` nécessaire pour la création du `.exe`
import atexit

#.#Déclaration des classes

#.##Classe `MenuApplication`
#.Cette classe hérite des classes `QMainWindow` et `Ui_Menu` et permet la 
#.création du GUI et toute sa gestion.  
#.Cette classe contient la majeure partie du programme du menu  
#.Elle est directement issue de *Qt* (et donc `PyQt`)
class MenuApplication(QMainWindow, Ui_Menu):
    #.###Méthode d'initialisation `__init__`
    #.Méthode permettant d'initialiser la classe
    def __init__(self, parent=None):
        #.On hérite de la méthode `__init__` des classes parentes
        super(MenuApplication, self).__init__(parent)
        #.On initialise les widgets décris dans le fichier auxiliaire 
        #.`ui_menu.py` créé avec *Qt Creator* et `PyQt`
        self.setupUi(self)

#.#Programme principal

#.##Fonction `main`
#.Fonction ne prenant pas d'arguments et permettant de créer l'interface et de 
#.la lancer
def main():
    #.On créé une application *Qt* `Qapplication`, pour porter notre GUI
    app = QApplication(sys.argv)
    #.On créé notre GUI comme étant une instance de la classe 
    #.`MenuApplication` décrite plus haut
    myapp = MenuApplication()
    #.On affiche notre GUI et on connecte sa fermeture à la fermeture du 
    #.programmme
    myapp.show()
    app.exec_()

#.##Test de lancement standalone
#.Test permettant de lancer le programme si il est exécuté directement tout 
#.seul, sans import
if __name__ == "__main__":
    #.On appelle la fonction `main` définit plus haut
    main()
