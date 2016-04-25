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
#.#Import des 3 modules pythons : `FenetreBVN`, `Menu` et `Module`
import fenetrebvn
import module

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

        self.param = []
        self.pseudo = ""

        self.BoutonCommencer.clicked.connect(self.commencer)
        self.BoutonQuitter.clicked.connect(self.quitter)

    def affFenetreBVN(self):
        self.FenetreBVN = fenetrebvn.FenetreBVNApplication()
        self.FenetreBVN.valeur_quitter.connect(self.handleQuitterBVN)
        self.FenetreBVN.termine.connect(self.termineBVN)
        self.FenetreBVN.setWindowModality(Qt.ApplicationModal)
        self.FenetreBVN.show()

    def getParam(self):
        temps = raw_input("Temps\n>>> ")
        if not temps:
            temps = 30
        else:
            temps = int(temps)
        texte_mode = raw_input("Mode texte\n>>> ")
        if not texte_mode:
            texte_mode = "expl::1"
        self.param = [temps, texte_mode]

    def getPseudo(self):
        pseudo = raw_input("Pseudo\n>>> ")
        if len(pseudo) > 20:
            pseudo = pseudo[:20]
        if not pseudo:
            pseudo = "Anonyme"
        self.pseudo = pseudo

    @pyqtSlot()
    def commencer(self):
        self.getParam()
        self.getPseudo()
        self.Module = module.ModuleApplication(self.param, self.pseudo)
        self.Module.termine.connect(self.termineModule)
        self.Module.setWindowModality(Qt.ApplicationModal)
        self.hide()
        self.Module.show()

    @pyqtSlot()
    def quitter(self):
        self.close()

    @pyqtSlot(bool)
    def handleQuitterBVN(self, valeur_quitter):
        if valeur_quitter:
            self.quitter()

    @pyqtSlot()
    def termineBVN(self):
        del self.FenetreBVN
        self.show()

    @pyqtSlot(bool)
    def termineModule(self, recommencerModule):
        del self.Module
        if recommencerModule:
            self.commencer()
        else:
            self.show()

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
    # #.On affiche notre GUI et on connecte sa fermeture à la fermeture du 
    # #.programmme
    myapp.affFenetreBVN()
    app.exec_()

    del myapp
    del app

#.##Test de lancement standalone
#.Test permettant de lancer le programme si il est exécuté directement tout 
#.seul, sans import
if __name__ == "__main__":
    #.On appelle la fonction `main` définit plus haut
    main()
