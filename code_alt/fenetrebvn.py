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
from ui_fenetrebvn import Ui_FenetreBVN
#.Import des bibliothèques standards de `python`
from time import time, sleep
import sys
#.Import de la biblothèque `re` pour l'utilisation d'expressions régulières
import re
#.Import de la bibliothèque `atexit` nécessaire pour la création du `.exe`
import atexit

#.#Déclaration des classes

#.##Classe `FenetreBVNApplication`
#.Cette classe hérite des classes `QMainWindow` et `Ui_FenetreBVN` et permet 
#.la création du GUI et toute sa gestion.  
#.Cette classe contient la majeure partie du programme de la fenêtre de 
#.bienvenue  
#.Elle est directement issue de *Qt* (et donc `PyQt`)
class FenetreBVNApplication(QMainWindow, Ui_FenetreBVN):
    valeur_quitter = pyqtSignal(bool)
    termine = pyqtSignal()
    #.###Méthode d'initialisation `__init__`
    #.Méthode permettant d'initialiser la classe

    def __init__(self, parent=None):
        #.On hérite de la méthode `__init__` des classes parentes
        super(FenetreBVNApplication, self).__init__(parent)
        #.On initialise les widgets décris dans le fichier auxiliaire 
        #.`ui_fenetrebvn.py` créé avec *Qt Creator* et `PyQt`
        self.setupUi(self)

        self.BoutonContinuer.clicked.connect(self.continuer)
        self.BoutonQuitter.clicked.connect(self.quitter)

    @pyqtSlot()
    def quitter(self):
        self.termine.emit()
        self.valeur_quitter.emit(True)
        self.close()

    @pyqtSlot()
    def continuer(self):
        self.termine.emit()
        self.valeur_quitter.emit(False)
        self.close()
