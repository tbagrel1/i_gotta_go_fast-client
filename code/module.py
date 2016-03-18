#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Import des modules

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_module import Ui_Module

# Déclaration des globales

# Paramètres importés de Menu à placer en argument de main()
temps_limite = True
temps_choisi = 30.0

corr_auto = True

mots_plus_utilises = True
nb_mots_plus_utilises = 100
texte = "Léo le cerf court dans la forêt"

# Autres global

der_car_T = ""
pos_texte = 0

# Déclaration des classes

class ModuleApplication(QMainWindow, Ui_Module):
    def __init__(self, parent=None):
        super(ModuleApplication, self).__init__(parent)
        self.setupUi(self)

        # On setup les widgets
        global texte

        # Ici on bind les signaux et les slots

        self.EntryTaper.textChanged.connect(self.getDerCar)

    # Ici on créer les slots et signaux persos

    def getDerCar(self, ligne_tapee):
        global der_car_T
        der_car_T = str((ligne_tapee[-1]).toUtf8())
        interpreterDerCar()

    def interpreterDerCar():
        global der_car_T
        #if der_car_T == 

# Programme principal

def main():
    app = QApplication(sys.argv)
    myapp = ModuleApplication()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
