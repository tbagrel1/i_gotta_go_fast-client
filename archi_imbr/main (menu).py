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
import os
import sys
#.Import de la biblothèque `re` pour l'utilisation d'expressions régulières
import re
#.Import de la bibliothèque `atexit` nécessaire pour la création du `.exe`
import atexit
#.#Import des 3 modules pythons : `FenetreBVN`, `Menu` et `Module`
import fenetrebvn
import module

import platform

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
        self.majTextesEx()

        self.tab_actuel = 1

        self.param = []
        self.pseudo = ""

        self.BoutonCommencer.clicked.connect(self.commencer)
        self.BoutonQuitter.clicked.connect(self.quitter)

        self.TabSourceTexte.currentChanged.connect(self.tabChange)

        self.SBoxMotsFR.valueChanged.connect(self.entryMotsFRCliquee)
        self.EntrySyll.textChanged.connect(self.entrySyllCliquee)

        self.CollerTexteV.textChanged.connect(self.entryCollerCliquee)
        self.NomTexteV.textChanged.connect(self.entryNomTexteCliquee)

    def majTextesEx(self):
        with open("exemple1.txt", "r") as fichier:
            titre1 = fichier.readline()[1:-1]
        with open("exemple2.txt", "r") as fichier:
            titre2 = fichier.readline()[1:-1]
        with open("exemple3.txt", "r") as fichier:
            titre3 = fichier.readline()[1:-1]
        self.LabelTexteEx1R.setText(titre1.decode("utf-8"))
        self.LabelTexteEx2R.setText(titre2.decode("utf-8"))
        self.LabelTexteEx3R.setText(titre3.decode("utf-8"))

    def affFenetreBVN(self):
        self.FenetreBVN = fenetrebvn.FenetreBVNApplication()
        self.FenetreBVN.valeur_quitter.connect(self.handleQuitterBVN)
        self.FenetreBVN.termine.connect(self.termineBVN)
        self.FenetreBVN.setWindowModality(Qt.ApplicationModal)
        self.FenetreBVN.show()

    def getParam(self):
        # Pour le temps
        temps = float(self.SBoxMinutes.value() * 60 +
                      self.SBoxSecondes.value())
        if temps == 0.0:
            temps = 60.0

        # Pour le texte
        if self.tab_actuel == 0:
            if self.RadioMotsFR.isChecked():
                nb_mots = self.SBoxMotsFR.value()
                texte_mode = "mots_fr::{}".format(nb_mots)
            elif self.RadioSyll.isChecked():
                syll = unicode(self.EntrySyll.text()).encode("utf-8").strip()
                if not syll:
                    syll = "ion"
                    self.EntrySyll.setText(u"ion")
                fichier_mots_brut = open("dictionnaire_syll.txt", "r")
                fichier_mots = fichier_mots_brut.readlines()
                liste_mots = [elt[:-1] for elt in fichier_mots if elt and
                              elt != "\n" and (syll in elt)]
                fichier_mots_brut.close()
                if len(liste_mots) < 25:
                    syll = "ion"
                    self.EntrySyll.setText(u"ion")
                texte_mode = "syll::{}".format(syll)
        if self.tab_actuel == 1:
            if self.LabelTexteEx1R.isChecked():
                texte_mode = "expl::1"
            elif self.LabelTexteEx2R.isChecked():
                texte_mode = "expl::2"
            elif self.LabelTexteEx3R.isChecked():
                texte_mode = "expl::3"
        if self.tab_actuel == 2:
            if self.CollerTexteR.isChecked():
                texte = unicode(self.CollerTexteV.toPlainText())\
                    .encode("utf-8").strip()
                texte = texte.replace("\n", " ").replace("  ", " ")
                if len(texte) > 4096:
                    texte = texte[:4096]
                    self.CollerTexteV.setPlainText(texte.decode("utf-8"))
                texte_mode = "perso::entier::{{{" + texte + "}}}"
            elif self.NomTexteR.isChecked():
                nom = unicode(self.NomTexteV.text()).encode("utf-8").strip()
                try:
                    fichier = open(nom, "r")
                    fichier.close()
                except:
                    nom = "texte.txt"
                    self.NomTexteV.setText(texte.decode("utf-8"))
                if platform.system() == "Linux" or platform.system() ==\
                   "Darwin":
                    if nom[0] != "/":
                        nom = os.getcwd() + "/" + nom
                elif platform.system() == "Windows":
                    if nom[1:3] != ":\\":
                        nom = os.getcwd() + "\\" + nom
                texte_mode = "perso::nom::{{{" + nom + "}}}"

        self.param = [temps, texte_mode]

    def getPseudo(self):
        pseudo = unicode(self.EntryPseudo.text()).encode("utf-8").strip()
        if not pseudo.strip():
            pseudo = "Anonyme"
        if len(pseudo) > 20:
            pseudo = pseudo[:20]
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

    @pyqtSlot(int)
    def tabChange(self, no):
        self.tab_actuel = no
        if self.tab_actuel == 0:
            # On clear le 2
            self.LabelTexteEx1R.setChecked(True)
            self.LabelTexteEx2R.setChecked(False)
            self.LabelTexteEx3R.setChecked(False)

            # On clear le 3
            self.CollerTexteR.setChecked(True)
            self.CollerTexteV.setPlainText("")
            self.NomTexteR.setChecked(False)
            self.NomTexteV.setText("")

        if self.tab_actuel == 1:
            # On clear le 1
            self.RadioMotsFR.setChecked(True)
            self.SBoxMotsFR.setValue(100)
            self.RadioSyll.setChecked(False)
            self.EntrySyll.setText("")

            # On clear le 3
            self.CollerTexteR.setChecked(True)
            self.CollerTexteV.setPlainText("")
            self.NomTexteR.setChecked(False)
            self.NomTexteV.setText("")

        if self.tab_actuel == 2:
            # On clear le 1
            self.RadioMotsFR.setChecked(True)
            self.SBoxMotsFR.setValue(100)
            self.RadioSyll.setChecked(False)
            self.EntrySyll.setText("")

            # On clear le 2
            self.LabelTexteEx1R.setChecked(True)
            self.LabelTexteEx2R.setChecked(False)
            self.LabelTexteEx3R.setChecked(False)

    @pyqtSlot()
    def entryMotsFRCliquee(self):
        if self.tab_actuel == 0:
            self.RadioMotsFR.setChecked(True)
            self.RadioSyll.setChecked(False)

    @pyqtSlot()
    def entrySyllCliquee(self):
        if self.tab_actuel == 0:
            self.RadioMotsFR.setChecked(False)
            self.RadioSyll.setChecked(True)

    @pyqtSlot()
    def entryCollerCliquee(self):
        if self.tab_actuel == 2:
            self.CollerTexteR.setChecked(True)
            self.NomTexteR.setChecked(False)

    @pyqtSlot()
    def entryNomTexteCliquee(self):
        if self.tab_actuel == 2:
            self.CollerTexteR.setChecked(False)
            self.NomTexteR.setChecked(True)

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
