#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Import des modules

from __future__ import division
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_module import Ui_Module
from time import time, sleep
from math import log
import sys
import atexit

# Déclaration des classes


class ThreadTimer(QThread):
    temps_fini_signal = pyqtSignal()
    temps_change_signal = pyqtSignal(float)
    finished = pyqtSignal()

    def __init__(self, temps_choisi):
        QThread.__init__(self)
        self.temps_choisi = temps_choisi
        self.temps_depart = 0.0
        self.temps_inter = 0.0
        self.temps_ecoule = 0.0
        self.temps_restant = 0.0
        self.jeton_quitter = False
        self.jeton_pause = True
        self.temps_debut_pause = 0.0
        self.temps_fin_pause = 0.0

    def run(self):
        # Il faut émit des signaux pour communiquer avec le prog principal
        self.temps_depart = time()
        self.jeton_pause = False
        while not self.jeton_quitter:
            self.temps_inter = time()
            self.temps_ecoule = self.temps_inter - self.temps_depart
            self.temps_restant = self.temps_choisi - self.temps_ecoule
            if self.temps_restant <= 0.0:
                self.temps_restant = 0.0
                self.temps_change_signal.emit(self.temps_restant)
                self.temps_fini_signal.emit()
                return
            else:
                self.temps_change_signal.emit(self.temps_restant)
                sleep(0.1)
            if self.jeton_pause:
                self.temps_debut_pause = time()
                while self.jeton_pause and not self.jeton_quitter:
                    sleep(0.1)
                self.temps_fin_pause = time()
                self.temps_pause_ecoule = (self.temps_fin_pause -
                                           self.temps_debut_pause)
                self.temps_depart += self.temps_pause_ecoule
        self.finished.emit()

    def pauseT(self):
        self.jeton_pause = True

    def reprendreT(self):
        self.jeton_pause = False

    def quitterT(self):
        self.jeton_quitter = True


class ModuleApplication(QMainWindow, Ui_Module):
    def __init__(self, parent=None):
        super(ModuleApplication, self).__init__(parent)
        self.setupUi(self)

        # Déclaration des globales
        self.jeton_pauseM = True
        self.temps_limite = True
        self.temps_choisi = 15.0
        self.texte = u"Léo le cerf court dans la forêt. Il rencontre ses amis \
au coin d'un ruisseau, et leur demande si ils vont bien. Ces derniers lui \
répondent par la négative : un de leurs frères a disparu !"
        self.texte = self.texte.replace("\n", " ")
        self.pos_texte = 0
        self.texte_d = self.texte[:self.pos_texte]
        self.texte_g = self.texte[(self.pos_texte + 1):]
        self.car_attendu = self.texte[self.pos_texte]
        self.temps_restant = 0.0
        self.premier_lancement_timer = True
        self.couleur_backup = ""
        self.jeton_temps_finiM = False
        self.s_mots = 0.0
        self.temps_ecoule = 0.0
        self.score = 0.0

        self.car_justes = 0
        self.car_faux = 0

        self.reussite = 0.0
        self.erreurs = 0.0

        self.Timer = ThreadTimer(self.temps_choisi)
        self.Timer.finished.connect(self.Timer.deleteLater)

        # On setup les widgets

        self.updateTexteLabel()
        self.temps_change(self.temps_choisi)

        # Ici on bind les signaux et les slots

        self.EntryTapeCentre.textChanged.connect(self.getDerCar)
        self.BoutonStartPause.clicked.connect(self.togglePauseM)
        self.BoutonQuitter.clicked.connect(self.quitterM)
        self.Timer.temps_change_signal.connect(self.temps_change)
        self.Timer.temps_fini_signal.connect(self.temps_fini)

        # On disable tant que pas commencé

        self.LabelTexteDroite.setEnabled(False)
        self.LabelTexteCentre.setEnabled(False)
        self.LabelTexteGauche.setEnabled(False)
        self.LabelTapeDroit.setEnabled(False)
        self.LabelTapeFleche.setEnabled(False)

        self.EntryTapeCentre.setFocus()

    # Ici on créer les slots et signaux persos

    @pyqtSlot(str)
    def getDerCar(self, ligne_tapee):
        der_car_T = unicode(ligne_tapee)
        self.EntryTapeCentre.clear()
        self.interpreterDerCar(der_car_T)
        if self.jeton_pauseM:
            self.togglePauseM()

    def interpreterDerCar(self, der_car_T):
        if der_car_T != "":
            if der_car_T == self.car_attendu:
                self.decalerTexte()
                self.car_justes += 1
                self.vert()
            else:
                self.car_faux += 1
                self.rouge()

    def vert(self):
        self.LabelTapeFleche.setStyleSheet("color: green")

    def rouge(self):
        self.LabelTapeFleche.setStyleSheet("color: red")

    def decalerTexte(self):
        self.pos_texte += 1
        self.texte_d = self.texte[:self.pos_texte]
        self.car_attendu = self.texte[self.pos_texte]
        self.texte_g = self.texte[(self.pos_texte + 1):]
        if (len(self.texte) - self.pos_texte) <= 23:
            self.texte += (u" " + self.texte)
            # On met à jour les labels
        self.updateTexteLabel()

    def updateTexteLabel(self):
        texte_aff_droite = self.texte_d
        if len(texte_aff_droite) > 22:
            texte_aff_droite = texte_aff_droite[-22:]
        texte_aff_centre = self.car_attendu
        texte_aff_gauche = self.texte_g
        if len(texte_aff_gauche) > 22:
            texte_aff_gauche = texte_aff_gauche[:22]
        texte_aff_basdroite = self.texte_d
        if len(texte_aff_basdroite) > 9:
            texte_aff_basdroite = texte_aff_basdroite[-9:]
        self.LabelTexteDroite.setText(texte_aff_droite)
        self.LabelTexteCentre.setText(texte_aff_centre)
        self.LabelTexteGauche.setText(texte_aff_gauche)
        self.LabelTapeDroit.setText(texte_aff_basdroite)

    @pyqtSlot()
    def togglePauseM(self):
        if self.jeton_temps_finiM:
            self.recommencer()
        elif self.premier_lancement_timer:
            self.premier_lancement_timer = False
            self.jeton_pauseM = False
            self.Timer.start()
            self.BoutonStartPause.setText(u"Pause")
            self.LabelTexteDroite.setEnabled(True)
            self.LabelTexteCentre.setEnabled(True)
            self.LabelTexteGauche.setEnabled(True)
            self.LabelTapeDroit.setEnabled(True)
            self.EntryTapeCentre.setFocus()
            self.LabelTapeFleche.setEnabled(True)
        else:
            if not self.jeton_pauseM:
                self.pauseM()
            elif self.jeton_pauseM:
                self.reprendreM()

    def pauseM(self):
        self.Timer.pauseT()
        self.BoutonStartPause.setText("Reprendre")
        self.jeton_pauseM = True
        # DISABLE
        self.LabelTexteDroite.setEnabled(False)
        self.LabelTexteCentre.setEnabled(False)
        self.LabelTexteGauche.setEnabled(False)
        self.LabelTapeDroit.setEnabled(False)
        self.LabelTapeFleche.setEnabled(False)
        self.EntryTapeCentre.setFocus()
        self.couleur_backup = self.LabelTapeFleche.styleSheet()
        self.LabelTapeFleche.setStyleSheet("")

    def reprendreM(self):
        self.Timer.reprendreT()
        self.BoutonStartPause.setText("Pause")
        self.jeton_pauseM = False
        self.LabelTexteDroite.setEnabled(True)
        self.LabelTexteCentre.setEnabled(True)
        self.LabelTexteGauche.setEnabled(True)
        self.LabelTapeDroit.setEnabled(True)
        self.EntryTapeCentre.setFocus()
        self.LabelTapeFleche.setEnabled(True)
        self.LabelTapeFleche.setStyleSheet(self.couleur_backup)

    @pyqtSlot()
    def quitterM(self):
        self.Timer.quitterT()
        self.Timer.wait()
        self.close()

    @pyqtSlot(float)
    def temps_change(self, temps_restant):
        self.temps_restant = temps_restant
        self.LabelRestantV.setText(unicode(
                                   "{} / {}"
                                   .format(round(self.temps_restant, 1),
                                           round(self.temps_choisi, 1))))
        self.BarreAvancement.setValue(int(round((self.temps_restant /
                                                 self.temps_choisi) * 100, 0)))
        self.genererStats()

    @pyqtSlot()
    def temps_fini(self):
        self.LabelTexteDroite.setEnabled(False)
        self.LabelTexteCentre.setEnabled(False)
        self.LabelTexteGauche.setEnabled(False)
        self.LabelTapeDroit.setEnabled(False)
        self.EntryTapeCentre.setEnabled(False)
        self.LabelTapeFleche.setStyleSheet("")
        self.LabelTapeFleche.setEnabled(False)
        self.jeton_temps_finiM = True
        self.setUpRecommencer()

    def setUpRecommencer(self):
        self.BoutonStartPause.setText("Recommencer")

    def recommencer(self):
        # A faire !!
        pass

    def genererStats(self):
        # On compte le nombre de mots
        self.compterMots()
        self.compterJusteErreur()
        self.compterScore()

    def compterMots(self):
        nombre_mots = len((self.texte_d).split(" ")) - 1
        self.LabelScoreV.setText(unicode(str(nombre_mots)))
        if nombre_mots <= 1:
            nombre_mots = 1
        self.temps_ecoule = self.temps_choisi - self.temps_restant
        self.s_mots = self.temps_ecoule / nombre_mots
        self.LabelSMotsV.setText(unicode(str(round(self.s_mots, 2))))

    def compterJusteErreur(self):
        somme = self.car_justes + self.car_faux
        if somme == 0:
            somme = 1
        self.reussite = self.car_justes / somme
        self.erreurs = self.car_faux / somme
        # print(erreurs)
        self.BarreReussite.setValue(round(self.reussite * 100, 0))
        self.BarreErreurs.setValue(round(self.erreurs * 100, 0))

    def compterScore(self):
        avancement = self.temps_ecoule / self.temps_choisi
        s_mots_mod = self.s_mots
        if s_mots_mod == 0:
            s_mots_mod = 1
        inv_vitesse = 1 / s_mots_mod
        erreurs_mod = self.erreurs
        if erreurs_mod == 0:
            erreurs_mod = 0.01
        ln_inv_erreurs = log(1 / erreurs_mod)
        ln_temps_plusC = log(self.temps_choisi / 60) + 5.5
        self.score = avancement * inv_vitesse * ln_inv_erreurs *\
            ln_temps_plusC * 100
        self.LabelScoreV.setText(unicode(str(int(round(self.score, 0)))))

# Programme principal


def main():  # On mettra des paramètres au main hérités du menu
    app = QApplication(sys.argv)
    myapp = ModuleApplication()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
