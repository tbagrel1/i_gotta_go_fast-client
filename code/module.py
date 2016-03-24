#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Import des modules

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_module import Ui_Module
from time import time, sleep

# Import toThread (A replier)
if True:  # Ajout du module threadTBAG
    from threading import *

    def static(var_name, value):
        def decorate(func):
            setattr(func, var_name, value)
            return func
        return decorate

    # Définition des classes et fonctions :
    class aThread(Thread):
        def __init__(self, threadID, name, command):
            Thread.__init__(self)
            self.threadID = threadID
            print("id: <{}>".format(self.threadID))
            self.name = name
            print("name: <{}>".format(self.name))
            self.command = command
            print("command: <{}>".format(self.command))

        def run(self):
            print("Starting " + self.name + " : " + str(self.threadID) +
                  " { " + self.command + " }")
            exec(self.command)
            print("Exiting " + self.name + " : " + str(self.threadID) +
                  " { " + self.command + " }")

    @static("c", 0)
    def toThread(name, command):
        exec("Thread_" + str(toThread.c) + " = aThread(" + str(toThread.c) +
             ", \"" + name + "\", \"" + command + "\")")
        exec("Thread_" + str(toThread.c) + ".daemon = True")
        exec("Thread_" + str(toThread.c) + ".start()")
        toThread.c += 1

# Déclaration des globales

# Paramètres importés de Menu à placer en argument de main()
temps_limite = True
temps_choisi = 30.0

corr_auto = True

mots_plus_utilises = True
nb_mots_plus_utilises = 100
texte = u"Léo le cerf court dans la forêt. Il rencontre ses amis au coin d\
'un ruisseau, et leur demande si ils vont bien. Ces derniers lui \
répondent par la négative : un de leurs frères a disparu !"

texte = texte.replace("\n", " ")

# Autres global

# Pour rappel, 22 caractères dans chaque boîte D / G en haut, plus 1 au
# centre -> 45
# 8 + 1 sur la ligne du bas

pos_texte = 0

texte_d = texte[:pos_texte]
texte_g = texte[(pos_texte + 1):]
car_attendu = texte[pos_texte]

print(texte_d, car_attendu, texte_g)

jeton_quitter = False
temps_depart = 0.0
temps_inter = 0.0
temps_ecoule = 0.0
temps_restant = 0.0
jeton_temps_valid = True
jeton_pause = False
temps_debut_pause = 0.0
temps_fin_pause = 0.0

# Déclaration des classes

# class ThreadTimer(QThread):
#     def __init__(self, temps_choisi):
#         Thread.__init__(self)
#         pause_active_signal = pyqtSignal()
#         pause_desactive_signal = pyqtSignal()
#         temps_fini_signal = pyqtSignal()
#         temps_change_signal = pyqtSignal(float)
#     def run(self):
#         # Il faut émit des signaux pour communiquer avec le prog principal
#         global jeton_quitter
#         global temps_depart
#         global temps_inter
#         global temps_ecoule
#         global temps_restant
#         global jeton_temps_valid
#         global jeton_pause
#         global temps_debut_pause
#         global temps_fin_pause
#         temps_debut = time()
#         while not jeton_quitter:
#             temps_inter = time()
#             temps_ecoule = temps_inter - temps_depart
#             temps_restant = temps_choisi - temps_ecoule
#             if jeton_pause:
#                 temps_debut_pause = time()
#                 ### EMIT PAUSE ACTIVE
#                 pause_active_signal.emit()
#                 while jeton_pause:
#                     sleep(0.1)
#                 temps_fin_pause = time()
#                 temps_pause_ecoule = temps_fin_pause - temps_debut_pause
#                 temps_depart += temps_pause_ecoule
#                 ### EMIT PAUSE DESACTIVE
#                 pause_desactive_signal.emit()
#             if temps_restant <= 0.0:
#                 ### EMIT FINI
#                 temps_fini_signal.emit()
#                 jeton_temps_valid = False
#             else:
#                 ### EMIT TEMPS_CHANGE -> return temps_restant
#                 temps_change_signal.emit(temps_restant)

class ModuleApplication(QMainWindow, Ui_Module):
    def __init__(self, parent=None):
        super(ModuleApplication, self).__init__(parent)
        self.setupUi(self)

        # On setup les widgets
        # global temps_choisi
        # self.Timer = ThreadTimer(temps_choisi)
        # self.Timer.daemon = True

        # Ici on bind les signaux et les slots

        self.EntryTapeCentre.textChanged.connect(self.getDerCar)
        self.updateTexteLabel()
        # self.BoutonStartPause.clicked.connect(self.premierLancementTimer)
        self.BoutonQuitter.clicked.connect(self.quitter)
        # self.Timer.pause_active_signal.connect()

    # Ici on créer les slots et signaux persos

    def getDerCar(self, ligne_tapee):
        der_car_T = unicode(ligne_tapee)
        self.EntryTapeCentre.clear()
        self.interpreterDerCar(der_car_T)

    def interpreterDerCar(self, der_car_T):
        global car_attendu
        if der_car_T == car_attendu:
            self.decalerTexte()
            self.vert()
        else:
            self.rouge()

    def vert(self):
        self.LabelTapeFleche.setStyleSheet("background-color: green")

    def rouge(self):
        self.LabelTapeFleche.setStyleSheet("background-color: red")

    def decalerTexte(self):
        global texte
        global pos_texte
        global texte_g
        global texte_d
        global car_attendu
        pos_texte += 1
        texte_d = texte[:pos_texte]
        car_attendu = texte[pos_texte]
        texte_g = texte[(pos_texte + 1):]
        if (len(texte) - pos_texte) <= 23:
            texte += (u" " + texte)
            # On met à jour les labels
        self.updateTexteLabel()

    def updateTexteLabel(self):
        global texte_d
        global texte_g
        global car_attendu
        texte_aff_droite = texte_d
        if len(texte_aff_droite) > 22:
            texte_aff_droite = texte_aff_droite[-22:]
        texte_aff_centre = car_attendu
        texte_aff_gauche = texte_g
        if len(texte_aff_gauche) > 22:
            texte_aff_gauche = texte_aff_gauche[:22]
        texte_aff_basdroite = texte_d
        if len(texte_aff_basdroite) > 9:
            texte_aff_basdroite = texte_aff_basdroite[-9:]
        self.LabelTexteDroite.setText(texte_aff_droite)
        self.LabelTexteCentre.setText(texte_aff_centre)
        self.LabelTexteGauche.setText(texte_aff_gauche)
        self.LabelTapeDroit.setText(texte_aff_basdroite)


    # def premierLancementTimer(self):
    #     self.Timer.start()
    #     self.BoutonStartPause.clicked.connect(self.Timer.togglePause)

    def quitter(self):
        global jeton_quitter
        jeton_quitter = True
        self.close()

# Programme principal

def main():
    app = QApplication(sys.argv)
    myapp = ModuleApplication()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
