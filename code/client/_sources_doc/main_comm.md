#Import des modules

##Imports `from`

Division décimale pour `Python 2`
```python
from __future__ import division
```
Interface graphique `PyQt4`
```python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtNetwork
```
Fichiers d'interfaces créés avec *Qt Creator*
```python
from _ui.ui_menu import Ui_Menu
from _ui.ui_module import Ui_Module
from _ui.ui_fenetrebvn import Ui_FenetreBVN
from _ui.ui_score import Ui_Score
```
Modules standars
```python
from time import time, sleep, localtime
from random import randint
from os import system, popen
from math import log
```
##Imports simples

Modules auxiliaires pour géner le cryptage
```python
import crypterScore
import crypterTexte
```
Module pour ouvrir des pages web
```python
import webbrowser
```
Modules standards
```python
import sys
import os
import pickle
import binascii
import re
import unicodedata
```
Modules nécessaires à la production de l'éxecutable
```python
import atexit
import platform
```
#Déclaration des classes

##Classe `FenetreBVNApplication`
Cette classe hérite des classes `QMainWindow` et `Ui_FenetreBVN` et permet 
la création du GUI et toute sa gestion.  
Cette classe contient la majeure partie du programme de la fenêtre de 
bienvenue  
Elle est directement issue de *Qt* (et donc `PyQt`)
```python
class FenetreBVNApplication(QMainWindow, Ui_FenetreBVN):
    valeur_quitter = pyqtSignal(bool)
    termine = pyqtSignal()
```
###Méthode d'initialisation `__init__`
Méthode permettant d'initialiser la classe
```python
    def __init__(self, parent=None):
```
On hérite de la méthode `__init__` des classes parentes
```python
        super(FenetreBVNApplication, self).__init__(parent)
```
On initialise les widgets décris dans le fichier auxiliaire 
`ui_fenetrebvn.py` créé avec *Qt Creator* et `PyQt`
```python
        self.setupUi(self)
```
On affiche le logo du programme dans la zone prévue
```python
        self.LabelIcone.setPixmap(QPixmap(os.getcwd() + "/img/logo1.png"))
```
On connecte les boutons à leurs slots respectifs
```python
        self.BoutonContinuer.clicked.connect(self.continuer)
        self.BoutonQuitter.clicked.connect(self.quitter)
```
###Méthode spéciale `keyPressEvent`
Méthode permettant de gérer les pressions de touches du clavier, prenant 
en paramètre `event`
```python
    def keyPressEvent(self, event):
```
Si l'événement correspond à une pression de touche
```python
        if type(event) == QKeyEvent:
```
Si la touche pressée est `<Escape>`
```python
            if event.key() == Qt.Key_Escape:
```
On appelle la méthode `quitter`
```python
                self.quitter()
```
Si la touche pressée est `<Return>` ou `<Space>`
```python
            elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Space:
```
On appelle la méthode `continuer`
```python
                self.continuer()
```
###Méthode (slot) `quitter`
Méthode permettant de quitter la fenêtre et le programme
```python
    @pyqtSlot()
    def quitter(self):
```
On émet le signal `termine`
```python
        self.termine.emit()
```
On émet le code de retour : `True` (quitter le programme)
```python
        self.valeur_quitter.emit(True)
```
On quitte la fenêtre
```python
        self.close()
```
###Méthode (slot) `continuer`
Méthode permettant de quitter la fenêtre mais de continuer le programme
```python
    @pyqtSlot()
    def continuer(self):
```
On émet le signal `termine`
```python
        self.termine.emit()
```
On émet le code de retour : `False` (continuer le programme)
```python
        self.valeur_quitter.emit(False)
```
On quitte la fenêtre
```python
        self.close()
```
##Classe `MenuApplication`
Cette classe hérite des classes `QMainWindow` et `Ui_Menu` et permet la 
création du GUI et toute sa gestion.  
Cette classe contient la majeure partie du programme du menu  
Elle est directement issue de *Qt* (et donc `PyQt`)
```python
class MenuApplication(QMainWindow, Ui_Menu):
```
###Méthode d'initialisation `__init__`
Méthode permettant d'initialiser la classe
```python
    def __init__(self, parent=None):
```
On hérite de la méthode `__init__` des classes parentes
```python
        super(MenuApplication, self).__init__(parent)
```
On initialise les widgets décris dans le fichier auxiliaire 
`ui_menu.py` créé avec *Qt Creator* et `PyQt`
```python
        self.setupUi(self)
```
On affiche le logo dans la zone prévue
```python
        self.LabelIcone.setPixmap(QPixmap(os.getcwd() + "/img/logo2.png"))
```
On appelle la méthode `majTextesEx` pour mettre à jour les titres 
des textes d'exemple
```python
        self.majTextesEx()
```
On définit l'onglet actuel comme le second (textes d'exemple)
```python
        self.tab_actuel = 1
```
On définit les attributs
```python
        self.param = []
        self.pseudo = ""
```
On connecte les boutons à leurs slots
```python
        self.BoutonCommencer.clicked.connect(self.commencer)
        self.BoutonQuitter.clicked.connect(self.quitter)
        self.BoutonAide.clicked.connect(self.ouvrirAide)
```
On connecte le changement d'onglet au slot correspondant
```python
        self.TabSourceTexte.currentChanged.connect(self.tabChange)
```
On connecte les changements de texte aux slots correspondants
```python
        self.SBoxMotsFR.valueChanged.connect(self.entryMotsFRCliquee)
        self.EntrySyll.textChanged.connect(self.entrySyllCliquee)
        self.CollerTexteV.textChanged.connect(self.entryCollerCliquee)
        self.NomTexteV.textChanged.connect(self.entryNomTexteCliquee)
```
###Méthode spéciale `keyPressEvent`
Méthode permettant de gérer les pressions de touches du clavier, prenant 
en paramètre `event`
```python
    def keyPressEvent(self, event):
```
Si l'événement correspond à une pression de touche
```python
        if type(event) == QKeyEvent:
```
Si la touche pressée est `<Escape>`
```python
            if event.key() == Qt.Key_Escape:
```
On appelle la méthode `quitter`
```python
                self.quitter()
```
Si la touche pressée est `<Return>`
```python
            elif event.key() == Qt.Key_Return:
```
On appelle la méthode `commencer`
```python
                self.commencer()
```
Si la touche pressée est `<F1>`
```python
            elif event.key() == Qt.Key_F1:
```
On appelle la méthode `ouvrirAide`
```python
                self.ouvrirAide()
```
###Méthode `majTextesEx`
Méthode permettant de mettre à jour les titres des textes d'exemple dans 
le menu
```python
    def majTextesEx(self):
```
On ouvre les 3 textes, et on ne conserve que la première ligne sans 
le `"#"`, qui correspond au titre
```python
        with open("txt/exemple1_e.txt", "r") as fichier:
            texte = crypterTexte.decrypterTexte(fichier.read())
            titre1 = texte.split("\n")[0][1:]
        with open("txt/exemple2_e.txt", "r") as fichier:
            texte = crypterTexte.decrypterTexte(fichier.read())
            titre2 = texte.split("\n")[0][1:]
        with open("txt/exemple3_e.txt", "r") as fichier:
            texte = crypterTexte.decrypterTexte(fichier.read())
            titre3 = texte.split("\n")[0][1:]
```
On affiche les nouveaux titres dans le menu
```python
        self.LabelTexteEx1R.setText(titre1.decode("utf-8"))
        self.LabelTexteEx2R.setText(titre2.decode("utf-8"))
        self.LabelTexteEx3R.setText(titre3.decode("utf-8"))
```
###Méthode (slot) `ouvrirAide`
Méthode permettant d'ouvrir le PDF d'aide
```python
    @pyqtSlot()
    def ouvrirAide(self):
```
On ouvre le PDF d'aide avec le navigateur internet
```python
        webbrowser.open("aide/aide.pdf")
```
###Méthode `affFenetreBVN`
Méthode appelée avant de `show` le menu et permettant de lancer la 
fenêtre de bienvenue
```python
    def affFenetreBVN(self):
```
On crée une nouvelle instance de la classe `FenetreBVNApplication`
```python
        self.FenetreBVN = FenetreBVNApplication()
```
On connecte le signal de retour et la fermeture de la fenêtre aux 
méthodes `handleQuitterBVN` et `termineBVN`
```python
        self.FenetreBVN.valeur_quitter.connect(self.handleQuitterBVN)
        self.FenetreBVN.termine.connect(self.termineBVN)
```
On affiche la fenêtre
```python
        self.FenetreBVN.setWindowModality(Qt.ApplicationModal)
        self.FenetreBVN.show()
```
On met à jour les scores en appelant la fonction 
`crypterScore.syncDB`
```python
        crypterScore.syncDB()
```
###Méthode `normaliserTexte`
Méthode permettant de normaliser un texte, en le recoupant à une taille 
limite et en remplaçant les caractères d'espacement
```python
    def normaliserTexte(self, texte):
```
On supprime les caractères d'espacement que l'on remplace par des 
espaces
```python
        texte = (re.sub(r"[\n\t\b\a\r]", r" ", texte)).strip()
```
On remplace ensuite les espaces multiples par un espace simple
```python
        texte = (re.sub(r" {2,}", r" ", texte.strip()))
```
On recoupe le texte si il est trop long
```python
        if len(texte) > 4096:
            texte = texte[:4096]
```
On renvoie le texte modifié
```python
        return texte
```
###Méthode `cheat`
Méthode permettant de détecter si le texte choisi est conforme (assez 
long, vrais mots...)
```python
    def cheat(self, texte):
```
On compte le nombre de mots et de caractères
```python
        mots = len(texte.split(" "))
        car = len(texte.replace(" ", ""))
```
On compte le nombre de caractères différents
```python
        car_d = []
        i = 0
        while len(car_d) < 5 and i < len(texte) - 1:
            c = texte[i]
            if c in car_d:
                pass
            else:
                car_d.append(c)
            i += 1
        nb_car_d = len(car_d)
```
On retourne un booléen correspondant aux conditions :  
- 5 mots minimum  
- 10 caractères minimum  
- 5 caractères différents minimum
```python
        return (mots < 5 or car < 10 or nb_car_d < 5)
```
###Méthode `getParam`
Méthode permettant de récupérer les différents paramètres de l'interface
```python
    def getParam(self):
```
On récupère le temps choisi que l'on exprime en secondes
```python
        temps = float(self.SBoxMinutes.value() * 60 +
                      self.SBoxSecondes.value())
```
Si le temps n'est pas conforme, on utilise les valeurs par défaut
```python
        if temps == 0.0:
            temps = 60.0
            self.SBoxMinutes.setValue(int(temps // 60))
            self.SBoxSecondes.setValue(int(temps % 60))
        elif temps <= 10.0 and self.pseudo.lower() != "admin":
            temps = 10.0
            self.SBoxMinutes.setValue(int(temps // 60))
            self.SBoxSecondes.setValue(int(temps % 60))
```
Si le premier onglet est l'onglet actif
```python
        if self.tab_actuel == 0:
```
Si *MotsFR* est choisi
```python
            if self.RadioMotsFR.isChecked():
```
On récupère la valeur pour *MotsFR*
```python
                nb_mots = self.SBoxMotsFR.value()
```
On définit le mode de texte : `"mots_fr::<val>"`
```python
                texte_mode = "mots_fr::{}".format(nb_mots)
```
Si *Syll* est choisi
```python
            elif self.RadioSyll.isChecked():
```
On récupère la syllabe entrée
```python
                syll = unicode(self.EntrySyll.text()).encode("utf-8").strip()
```
Si rien n'est rentré, on utilise une valeur par défaut
```python
                if not syll:
                    syll = "ion"
                    self.EntrySyll.setText(u"ion")
```
On ouvre le dictionnaire de référence et on récupère le 
contenu
```python
                fichier_mots_brut = open("txt/dictionnaire_syll_e.txt", "r")
                fichier_mots =\
                    crypterTexte.decrypterTexte(fichier_mots_brut.read())
                fichier_mots = fichier_mots.split("\n")
                liste_mots = [elt for elt in fichier_mots if elt and
                              (syll in elt)]
                fichier_mots_brut.close()
```
Si moins de 25 mots du dictionnaire possèdent la syllabe 
entée, on utilise la valeur par défaut
```python
                if len(liste_mots) < 25:
                    syll = "ion"
                    self.EntrySyll.setText(u"ion")
```
On définit le mode de texte : `"syll::<val>"`
```python
                texte_mode = "syll::{}".format(syll)
```
Si le deuxième onglet est l'onglet actif
```python
        if self.tab_actuel == 1:
```
Si le texte d'exemple 1 est choisi
```python
            if self.LabelTexteEx1R.isChecked():
```
On définit le mode de texte : `"expl::1"`
```python
                texte_mode = "expl::1"
```
Si le texte d'exemple 2 est choisi
```python
            elif self.LabelTexteEx2R.isChecked():
```
On définit le mode de texte : `"expl::1"`
```python
                texte_mode = "expl::2"
```
Si le texte d'exemple 3 est choisi
```python
            elif self.LabelTexteEx3R.isChecked():
```
On définit le mode de texte : `"expl::1"`
```python
                texte_mode = "expl::3"
```
Si le troisième onglet est l'onglet actif
```python
        if self.tab_actuel == 2:
```
Si *Texte à copier-coller* est choisi
```python
            if self.CollerTexteR.isChecked():
```
On récupère le texte entré
```python
                texte = unicode(self.CollerTexteV.toPlainText())\
                    .encode("utf-8").strip()
```
Si le texte normalisé n'est pas conforme
```python
                if self.cheat(self.normaliserTexte(texte)):
```
On utilise des valeurs par défaut : texte d'exemple 1
```python
                    texte_mode = "expl::1"
```
Si le texte est conforme
```python
                else:
```
On définit le mode de texte : 
`"perso::entier::{{{<val>}}}"`
```python
                    texte_mode = "perso::entier::{{{" + texte + "}}}"
```
Si *Texte choisi par nom* est choisi
```python
            elif self.NomTexteR.isChecked():
```
On récupère le nom
```python
                nom = unicode(self.NomTexteV.text()).encode("utf-8").strip()
```
On essaye
```python
                try:
```
On ouvre le fichier
```python
                    fichier_brut = open("txt/" + nom, "r")
```
On lit et noramlise le texte
```python
                    fichier = self.normaliserTexte(fichier_brut.read())
```
On ferme le fichier
```python
                    fichier_brut.close()
```
On lève une exception si le texte normalisé n'est pas 
conforme
```python
                    if self.cheat(fichier):
                        raise TricheError
```
Si tout est passé, on défini le mode de texte : 
`"perso::nom::{{{<val>}}}"`
```python
                    texte_mode = "perso::nom::{{{" + nom + "}}}"
```
Si une exception a été levée (il y a eu une erreur)
```python
                except:
```
On utilise des valeurs par défaut : texte d'exemple 1
```python
                    texte_mode = "expl::1"
```
On met à jour l'attribut-liste `param` avec les nouvelles valeurs 
du temps et du mode de texte
```python
        self.param = [temps, texte_mode]
```
###Méthode `getPseudo`
Méthode permettant de récupérer le pseudo saisi par l'utilisateur
```python
    def getPseudo(self):
```
On récupère le pseudo entré
```python
        pseudo = unicode(self.EntryPseudo.text()).encode("utf-8").strip()
```
Si aucun pseudo n'est entré, on choisit `"Anonyme"`
```python
        if not pseudo.strip():
            pseudo = "Anonyme"
```
Si le pseudo est trop long, on le recoupe à 20 caractères
```python
        if len(pseudo) > 20:
            pseudo = pseudo[:20]
```
On met à jour la valeur de l'attribut `pseudo`
```python
        self.pseudo = pseudo
```
###Méthode (slot) `commencer`
Méthode permettant de lancer une partie et donc d'afficher une fenêtre 
de *Module*
```python
    @pyqtSlot()
    def commencer(self):
```
On récupère les paramètres et le pseudo
```python
        self.getParam()
        self.getPseudo()
```
On créé une instance de `ModuleApplication`, en passant les 
paramètres et le pseudo au constructeur
```python
        self.Module = ModuleApplication(self.param, self.pseudo)
```
On connecte le signal `termine` de la nouvelle fenêtre à la bonne 
méthode
```python
        self.Module.termine.connect(self.termineModule)
```
On prépare la nouvelle fenêtre, on cache le menu et on affiche la 
nouvelle fenêtre
```python
        self.Module.setWindowModality(Qt.ApplicationModal)
        self.hide()
        self.Module.show()
```
###Méthode (slot) `quitter`
Méthode permettant de quitter le menu et donc le programme
```python
    @pyqtSlot()
    def quitter(self):
```
On ferme la fenêtre menu
```python
        self.close()
```
###Méthode (slot) `handleQuitterBVN`
Méthode prenant en paramètre la valeur de retour de la fenêtre BVN et 
permettant soit de continuer, soit de quitter le programme
```python
    @pyqtSlot(bool)
    def handleQuitterBVN(self, valeur_quitter):
```
Si le code de retour vaut `True`
```python
        if valeur_quitter:
```
On quitte le menu donc le programme
```python
            self.quitter()
```
###Méthode (slot) `termineBVN`
Méthode permettant de gérer la fermeture de la fenêtre BVN
```python
    @pyqtSlot()
    def termineBVN(self):
```
On détruit l'instance en cours de fenêtre BVN, pour éviter les 
collisions
```python
        del self.FenetreBVN
```
On réaffiche le menu
```python
        self.show()
```
###Méthode (slot) `termineModule`
Méthode prenant en paramètre le code de retour de la fenêtre du module 
et permettant soit de recommencer une partie identique, soit de 
réafficher le menu
```python
    @pyqtSlot(bool)
    def termineModule(self, recommencerModule):
```
On supprime l'instance en cours de la fenêtre du module, pour éviter 
les collisions
```python
        del self.Module
```
Si le code de retour pour recommencer vaut `True`
```python
        if recommencerModule:
```
On réappelle la méthode `commencer`
```python
            self.commencer()
```
Sinon (si l'utilisateur ne veut pas recommencer)
```python
        else:
```
On réaffiche le menu
```python
            self.show()
```
###Méthode (slot) `tabChange`
Méthode permettant de gérer le changement d'onglet pour le choix du 
texte et prenant en paramètre le nouveau numéro de l'onglet (0, 1 ou 2)
```python
    @pyqtSlot(int)
    def tabChange(self, no):
        self.tab_actuel = no
```
Si l'onglet actif est le premier
```python
        if self.tab_actuel == 0:
```
On remet aux valeurs par défaut le deuxième
```python
            self.LabelTexteEx1R.setChecked(True)
            self.LabelTexteEx2R.setChecked(False)
            self.LabelTexteEx3R.setChecked(False)
```
On remet aux valeurs par défaut le troisième
```python
            self.CollerTexteR.setChecked(True)
            self.CollerTexteV.setPlainText("")
            self.NomTexteR.setChecked(False)
            self.NomTexteV.setText("")
```
Si l'onglet actif est le deuxième
```python
        if self.tab_actuel == 1:
```
On remet aux valeurs par défaut le premier
```python
            self.RadioMotsFR.setChecked(True)
            self.SBoxMotsFR.setValue(100)
            self.RadioSyll.setChecked(False)
            self.EntrySyll.setText("")
```
On remet aux valeurs par défaut le troisième
```python
            self.CollerTexteR.setChecked(True)
            self.CollerTexteV.setPlainText("")
            self.NomTexteR.setChecked(False)
            self.NomTexteV.setText("")
```
Si l'onglet actif est le troisième
```python
        if self.tab_actuel == 2:
```
On remet aux valeurs par défaut le premier
```python
            self.RadioMotsFR.setChecked(True)
            self.SBoxMotsFR.setValue(100)
            self.RadioSyll.setChecked(False)
            self.EntrySyll.setText("")
```
On remet aux valeurs par défaut le deuxième
```python
            self.LabelTexteEx1R.setChecked(True)
            self.LabelTexteEx2R.setChecked(False)
            self.LabelTexteEx3R.setChecked(False)
```
###Méthode (slot) `entryMotsFRCliquee`
Méthode permettant de changer la valeur du choix quand du texte est 
entré dans la boîte de texte *Mots FR*
```python
    @pyqtSlot()
    def entryMotsFRCliquee(self):
```
Si l'onglet actif est le premier (pour éviter de déclencher la 
méthode lors de la remise par défaut des onglets non actifs)
```python
        if self.tab_actuel == 0:
```
On met le choix *Mots FR* à `True`
```python
            self.RadioMotsFR.setChecked(True)
```
On met le choix *Syll* à `False`
```python
            self.RadioSyll.setChecked(False)
```
###Méthode (slot) `entrySyllCliquee`
Méthode permettant de changer la valeur du choix quand du texte est 
entré dans la boîte de texte *Syll*
```python
    @pyqtSlot()
    def entrySyllCliquee(self):
```
Si l'onglet actif est le premier (pour éviter de déclencher la 
méthode lors de la remise par défaut des onglets non actifs)
```python
        if self.tab_actuel == 0:
```
On met le choix *Mots FR* à `False`
```python
            self.RadioMotsFR.setChecked(False)
```
On met le choix *Syll* à `True`
```python
            self.RadioSyll.setChecked(True)
```
Méthode (slot) `entryCollerCliquee`
Méthode permettant de changer la valeur du choix quand du texte est
entré dans la boîte de texte *Texte copié-collé*
```python
    @pyqtSlot()
    def entryCollerCliquee(self):
```
Si l'onglet actif est le troisième (pour éviter de déclencher la 
méthode lors de la remise par défaut des onglets non actifs)
```python
        if self.tab_actuel == 2:
```
On met le choix *Texte copié-collé* à `True`
```python
            self.CollerTexteR.setChecked(True)
```
On met le choix *Texte par nom* à `False`
```python
            self.NomTexteR.setChecked(False)
```
Méthode (slot) `entryNomTexteCliquee`
Méthode permettant de changer la valeur du choix quand du texte est 
entré dans la boîte de texte *Texte par nom*
```python
    @pyqtSlot()
    def entryNomTexteCliquee(self):
```
Si l'onglet actif est le troisième (pour éviter de déclencher la 
méthode lors de la remise par défaut des onglets non actifs)
```python
        if self.tab_actuel == 2:
```
On met le choix *Texte copié-collé* à `False`
```python
            self.CollerTexteR.setChecked(False)
```
On met le choix *Texte par nom* à `True`
```python
            self.NomTexteR.setChecked(True)
```
##Classe `ModuleApplication`
Cette classe hérite des classes `QMainWindow` et `Ui_Module` et permet la 
création du GUI et toute sa gestion.  
Cette classe contient la majeure partie du programme du module  
Elle est directement issue de *Qt* (et donc `PyQt`)
```python
class ModuleApplication(QMainWindow, Ui_Module):
    termine = pyqtSignal(bool)
```
###Méthode d'initialisation `__init__`  
Méthode permettant d'initialiser la classe
```python
    def __init__(self, param=[60, "expl::1"], pseudo="Anonyme", parent=None):
```
On hérite de la méthode `__init__` des classes parentes
```python
        super(ModuleApplication, self).__init__(parent)
```
On initialise les widgets décris dans le fichier auxiliaire 
`ui_module.py` créé avec *Qt Creator* et `PyQt`
```python
        self.setupUi(self)
```
On part du principe que les paramètres auront été vérifiés par le
menu et qu'ils sont donc exempts d'erreurs

```python
        self.temps_choisi = param[0]
        self.mode_texte = param[1]
        self.pseudo = pseudo

        self.texte = ""
        self.genererTexte()
```
On définit les attributs
```python
        self.recommencerV = False
        self.pos_texte = 0
        self.texte_d = self.texte[:self.pos_texte]
        self.texte_g = self.texte[(self.pos_texte + 1):]
        self.car_attendu = self.texte[self.pos_texte]
        self.der_car_T = ""
        self.dernier_juste = False
        self.jeton_pauseM = True
        self.temps_restant = 0.0
        self.premier_lancement_timer = True
        self.couleur_backup = ""
        self.jeton_temps_finiM = False
        self.mots_min = 0.0
        self.car_min = 0.0
        self.temps_ecoule = 0.0
        self.score = 0.0
        self.temps_score_precedant = 0.0
        self.C_TEMPS = 5
        self.C_SCORE = 10
        self.car_justes = 0
        self.car_faux = 0
        self.car_faux_precedant = 0
        self.reussite = 0.0
        self.erreurs = 0.0
        self.nombre_mots_precedant = 0
        self.car_attendu_precedant = ""
        self.coeff_pre = 1.0
```
On créé l'attribut `Timer`, qui est une instance du `ThreadTimer` 
déclaré plus haut.  
On lui passe en argument le temps choisi dans le fichier de 
configuration
```python
        self.Timer = ThreadTimer(self.temps_choisi)
```
On connecte le signal `finished` du timer à la méthode en charge de 
le détruire proprement
```python
        self.Timer.finished.connect(self.Timer.deleteLater)
```
On lance une première fois les méthodes `updateTexteLabel` et 
`temps_change` pour régler le GUI sur la position de départ
```python
        self.updateTexteLabel()
        self.temps_change(self.temps_choisi)
        self.meilleursScores()
```
On fixe la police des labels en police à chasse fixe (monospace)  
Cela permet d'éviter l'erreur avec Windows qui ne reconnait pas la 
police `Monospace`
```python
        Police = QFont("Monospace", 30)
        Police.setStyleHint(QFont.TypeWriter)
        self.LabelTexteDroite.setFont(Police)
        self.LabelTexteCentre.setFont(Police)
        self.LabelTexteGauche.setFont(Police)
        self.LabelTapeDroit.setFont(Police)
        self.EntryTapeCentre.setFont(Police)
```
Quand le texte dans la boîte est changé (frappe de l'utilisateur), 
on appelle la méthode `getDerCar` en charge de récupérer la saisie
```python
        self.EntryTapeCentre.textChanged.connect(self.getDerCar)
```
Quand on clique sur le bouton start/pause, on appelle la méthode 
`togglePauseM` en charge du basculement start/pause
```python
        self.BoutonStartPause.clicked.connect(self.togglePauseM)
```
Quand on clique sur le bouton quitter, on appelle la méthode
`quitterM` en charge de fermer proprement le timer avant de quitter 
le GUI
```python
        self.BoutonQuitter.clicked.connect(self.quitterM)
```
On connecte les signaux du timer `temps_change` et `temps_fini` aux 
méthodes du GUI associées, qui servent à interpréter quand le temps 
restant change et quand le temps est fini
```python
        self.Timer.temps_change_signal.connect(self.temps_change)
        self.Timer.temps_fini_signal.connect(self.temps_fini)
```
On désactive les widgets tant que l'utilisateur ne clique pas sur 
commencer ou qu'il ne tape pas de lettre
```python
        self.LabelTexteDroite.setEnabled(False)
        self.LabelTexteCentre.setEnabled(False)
        self.LabelTexteGauche.setEnabled(False)
        self.LabelTapeDroit.setEnabled(False)
        self.LabelTapeFleche.setEnabled(False)
```
On active le focus sur la boîte de texte (comme ça l'utilisateur n'a 
pas à cliquer dessus)
```python
        self.EntryTapeCentre.setFocus()
```
###Méthode `meilleursScores`
Méthode permettant d'afficher les meilleurs scores dans le tableau en 
bas à droite
```python
    def meilleursScores(self):
```
On appelle la méthode `trouverMeilleursScores`
```python
        meilleurs = self.trouverMeilleursScores()
```
On affiche les valeurs obtenues
```python
        self.LabelMeilleur1.setText(unicode(str(meilleurs[0])))
        self.LabelMeilleur2.setText(unicode(str(meilleurs[1])))
        self.LabelMeilleur3.setText(unicode(str(meilleurs[2])))
```
###Méthode `trouverMeilleursScores`
Méthode permettant de trouver les 3 meilleurs scores spéciaux à partir 
de la DB locale
```python
    def trouverMeilleursScores(self):
```
On essaye
```python
        try:
```
On ouvre le fichier de la DB locale
```python
            fichier_db = open("score/local_db.db", "rb")
```
On récupère le contenu avec un pickler
```python
            mon_pickler = pickle.Unpickler(fichier_db)
            liste = mon_pickler.load()
            fichier_db.close()
```
Si l'objet récupéré est vide ou `None`
```python
            if not liste:
```
On lève l'exception `VideException`
```python
                raise VideException
```
On recherche d'abord le meilleur score absolu
```python
            pas_encore_trouve_best = True
            i = 0
            best = None
```
Tant que l'on ne l'a pas trouvé et que la liste n'est pas finie
```python
            while pas_encore_trouve_best and i < len(liste) - 1:
```
Si le pseudo ne commence pas par `"#"`
```python
                if liste[i]["pseudo"][0] != "#":
```
On considère que c'est le meilleur score
```python
                    pas_encore_trouve_best = False
                    best = liste[i]["score"]
                i += 1
```
Si aucune valeur n'a été trouvée (la DB est vide ou incorrecte), 
on lève l'exception `VideException`
```python
            if not best:
                raise VideException
```
On recherche ensuite le meilleur score dans le même mode
```python
            pas_encore_trouve_best_mode = True
            i = 0
            best_mode = None
```
Tant que l'on ne l'a pas trouvé et que la liste n'est pas finie
```python
            while pas_encore_trouve_best_mode and i < len(liste) - 1:
```
Si le pseudo ne commence pas par `"#"`
```python
                if liste[i]["pseudo"][0] != "#":
```
Si le mode du score examiné est le même que le score 
réalisé
```python
                    if str(liste[i]["texte_mode_enh"]) == self.modeTexteEnh():
```
On considère que c'est le meilleur score pour le 
mode choisi
```python
                        pas_encore_trouve_best_mode = False
                        best_mode = liste[i]["score"]
                i += 1
```
Si aucune valeur n'a été trouvée (aucune partie dans le même 
mode dans la DB ou DB incorrecte)
```python
            if not best_mode:
```
On met `"..."` à la place du meilleur score dans le mode en 
cours
```python
                best_mode = "..."
```
On recherche enfin le meilleur score pour le pseudo en cours
```python
            pas_encore_trouve_best_perso = True
            i = 0
            best_perso = None
```
Tant que l'on ne l'a pas trouvé et que la liste n'est oas finie
```python
            while pas_encore_trouve_best_perso and i < len(liste) - 1:
```
Si le pseudo ne commence pas par `"#"`
```python
                if liste[i]["pseudo"][0] != "#":
```
Si le pseudo du score examiné correspond au pseudo de 
l'utilisateur
```python
                    if str(liste[i]["pseudo"]) == self.pseudo:
```
On considère que c'est le meilleur score de 
l'utilisateur
```python
                        pas_encore_trouve_best_perso = False
                        best_perso = liste[i]["score"]
                i += 1
```
Si aucune valeur n'a été trouvée (le joueur n'a jamais joué ou 
la DB est incorrecte)
```python
            if not best_perso:
```
On met `"..."` à la place du meilleur score du joueur
```python
                best_perso = "..."
```
Enfin, on retourne les 3 valeurs de scores calculées
```python
            return (best, best_mode, best_perso)
```
Si une exception a été levée (pas de DB, ou DB incorrecte, ou aucun 
score dans la DB)
```python
        except:
```
On retourne une liste de 3 chaînes `"..."`
```python
            return ("...", "...", "...")

    def modeTexteEnh(self):
        mode_texte_enh = ""
        mds = self.mode_texte.split("::")
        if mds[0] == "expl":
            mode_texte_enh = "Texte d'exemple {}"\
                .format(mds[1])
        elif mds[0] == "syll":
            mode_texte_enh = "Mots avec la syllabe -{}"\
                .format(mds[1])
        elif mds[0] == "mots_fr":
            mode_texte_enh = "Les {} mots les plus courants"\
                .format(mds[1])
        elif mds[0] == "perso":
            if mds[1] == "nom":
                mode_texte_enh = "Texte personnalisé : \"{}\""\
                    .format(mds[2][3:-3].split("/")[-1])
            elif mds[1] == "entier":
                mode_texte_enh = "Texte personnalisé : {}..."\
                    .format(mds[2][3:-3][:min(10, len(mds[2][3:-3]))])
        else:
            mode_texte_enh = "Inconnu"
        return mode_texte_enh

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_Escape:
                self.quitterM()
            elif event.key() == Qt.Key_Return:
                self.togglePauseM()

    def genererTexte(self):
        mtxt_s = self.mode_texte.split("::")
        if mtxt_s[0] == "mots_fr":
            self.texte += (self.genererMotsFR(int(mtxt_s[1]))).decode("utf-8")
        elif mtxt_s[0] == "syll":
            self.texte += (self.genererSyll(mtxt_s[1])).decode("utf-8")
        elif mtxt_s[0] == "expl":
            self.texte += (self.genererExemple(int(mtxt_s[1]))).decode("utf-8")
        elif mtxt_s[0] == "perso":
            if mtxt_s[1] == "nom":
                self.texte += (self.genererNom((mtxt_s[2])[3:-3]))\
                    .decode("utf-8")
            elif mtxt_s[1] == "entier":
                self.texte += (self.genererEntier((mtxt_s[2])[3:-3]))\
                    .decode("utf-8")

    def genererMotsFR(self, nb):
        fichier_mots_brut = open("txt/dictionnaire_freq_e.txt", "r")
        fichier_mots = crypterTexte.decrypterTexte(fichier_mots_brut.read())
        fichier_mots = fichier_mots.split("\n")
        fichier_mots_brut.close()
        liste_mots = [elt for elt in fichier_mots if elt][:nb]
        chaine = ""
        for i in range(25):
            j = randint(0, nb - 1)
            chaine += (liste_mots[j] + " ")
        return chaine

    def genererSyll(self, syll):
        fichier_mots_brut = open("txt/dictionnaire_syll_e.txt", "r")
        fichier_mots = crypterTexte.decrypterTexte(fichier_mots_brut.read())
        fichier_mots = fichier_mots.split("\n")
        fichier_mots_brut.close()
        liste_mots = [elt for elt in fichier_mots if elt and (syll in elt)]
        chaine = ""
        for i in range(25):
            j = randint(0, len(liste_mots) - 1)
            chaine += (liste_mots[j] + " ")
        return chaine

    def genererExemple(self, no):
        exec("fichier_brut = open(\"txt/exemple{}_e.txt\", \"r\")".format(no))
        fichier = crypterTexte.decrypterTexte(fichier_brut.read())
        fichier = fichier.split("\n")
        texte = ""
        for ligne in fichier:
            if ligne:
                if ligne[0] != "#":
                    texte += (ligne + "\n")
        return (self.normaliserTexte(texte) + " ")

    def genererNom(self, nom):
        fichier_brut = open("txt/" + nom, "r")
        fichier = fichier_brut.read()
        fichier_brut.close()
        return (self.normaliserTexte(fichier) + " ")

    def genererEntier(self, texte):
        return (self.normaliserTexte(texte) + " ")

    def normaliserTexte(self, texte):
        texte = (re.sub(r"[\n\t\b\a\r]", r" ", texte)).strip()
        texte = (re.sub(r" {2,}", r" ", texte.strip()))
        if len(texte) > 4096:
            texte = texte[:4096]
        return texte
```
###Méthode (slot) `getDerCar`
Méthode permettant de récupérer le caractère tapé dans la boîte de texte 
suite à un signal `textChanged`
```python
    @pyqtSlot(str)
    def getDerCar(self, ligne_tapee):
```
On récupère le caractère tapé, on vide la boîte et appelle la 
méthode `interpreterDerCar` pour interpréter le caractère tapé
```python
        self.der_car_T = ligne_tapee
        self.interpreterDerCar()
        self.EntryTapeCentre.clear()
```
Si `jeton_pauseM` vaut `True` (le programme était en pause ou pas 
encore commencé et l'utilisateur a tapé une lettre), on appelle 
la méthode `togglePauseM` pour désactiver la pause
```python
        if self.jeton_pauseM:
            self.togglePauseM()
```
###Méthode `interpreterDerCar`
Méthode permettant d'interpréter le caractère tapé à la suite de la 
méthode `getDerCar`
```python
    def interpreterDerCar(self):
```
On vérifie que le texte tapé n'est pas nul (car les méthodes 
`getDerCar` et `interpreterDerCar` se déclenchent après le `clear`
 de la boîte)
```python
        if self.der_car_T != "":
```
On calcule les caractères normalisés
```python
            car_attendu_dec = unicodedata.normalize('NFKD', self.car_attendu)
            car_attendu_norm = car_attendu_dec.encode('ascii', 'ignore')
            car_attendu_norm = unicode(car_attendu_norm)
```
Si le caractère tapé est bien le caractère attendu :  
On appelle la méthode `decalerTexte`, on ajoute 1 aux caractères 
justes et on met en vert les flèches (méthode `vert`)
```python
            self.der_car_T = self.der_car_T[0]
            if self.der_car_T == self.car_attendu:
                self.coeff_pre = 1.0
                self.dernier_juste = True
                self.car_attendu_precedant = self.car_attendu
                self.car_justes += 1
                self.vert()
                self.decalerTexte()
            # À faire
            elif self.der_car_T == "$":
                self.coeff_pre = 0.0
                self.dernier_juste = True
                self.car_attendu_precedant = self.car_attendu
                self.LabelTapeFleche.setStyleSheet("")
                self.decalerTexte()
            # Si caractère normalisé :
            elif self.der_car_T == self.car_attendu.lower() or\
                self.der_car_T == car_attendu_norm or\
                    self.der_car_T == car_attendu_norm.lower():
                self.coeff_pre = 0.25
                self.dernier_juste = True
                self.car_attendu_precedant = self.car_attendu
                self.vert()
                self.decalerTexte()
```
Sinon :  
On ajoute 1 aux caractères faux et on met en rouge les flèches
(méthode `rouge`)
```python
            else:
                self.dernier_juste = False
                self.car_faux += 1
                self.rouge()
```
Enfin, on appelle la méthode `genererStats` pour mettre à jour 
les statistiques
```python
            self.genererStats()
```
###Méthode `vert`
Méthode permettant de mettre en vert les flèches (`LabelTapeFleche`)
```python
    def vert(self):
```
On définit la couleur de police à `green`
```python
        self.LabelTapeFleche.setStyleSheet("color: green")
```
###Méthode `rouge`
Méthode permettant de mettre en rouge les flèches (`LabelTapeFleche`)
```python
    def rouge(self):
```
On définit la couleur de police à `red`
```python
        self.LabelTapeFleche.setStyleSheet("color: red")
```
###Méthode `decalerTexte`
Méthode permettant de décaler le texte (au niveau des variables)
```python
    def decalerTexte(self):
```
On avance de 1 la variable `pos_texte` ;  
On actualise les variables `texte_d`, `texte_g` et `car_attendu`
en fonction de la nouvelle valeur de `pos_texte`
```python
        self.pos_texte += 1
        self.texte_d = self.texte[:self.pos_texte]
        self.car_attendu = self.texte[self.pos_texte]
        self.texte_g = self.texte[(self.pos_texte + 1):]
```
Si on est bientôt à cours de texte dans la partie droite 
(`texte_g`), on double le texte (on le reboucle sur lui-même)
```python
        if (len(self.texte) - self.pos_texte) <= 23:
            self.genererTexte()
```
Enfin, on met à jour les labels
```python
        self.updateTexteLabel()
```
###Méthode `updateTexteLabel`
Méthode permettant de mettre à jour le texte des labels du GUI (et donc 
décaler le texte au niveau du GUI)
```python
    def updateTexteLabel(self):
```
La variable `texte_aff_droite` correspond à `texte_d` recoupé si 
besoin à la longueur maximum du label (22 caractères)
```python
        texte_aff_droite = self.texte_d
        if len(texte_aff_droite) > 22:
            texte_aff_droite = texte_aff_droite[-22:]
```
La variable `texte_aff_centre` correspond au caractère attendu
```python
        texte_aff_centre = self.car_attendu
```
La variable `texte_aff_gauche` correspond à `texte_g` recoupé si 
besoin à la longueur maximum du label (22 caractères)
```python
        texte_aff_gauche = self.texte_g
        if len(texte_aff_gauche) > 22:
            texte_aff_gauche = texte_aff_gauche[:22]
```
La variable `texte_aff_basdroite` correspond à `texte_d` recoupé si 
besoin à la longueur maximum du label (9 caractères)
```python
        texte_aff_basdroite = self.texte_d
        if len(texte_aff_basdroite) > 9:
            texte_aff_basdroite = texte_aff_basdroite[-9:]
```
Ensuite, on met à jour les labels avec les nouvelles valeurs des 
variables évoqués ci-dessus
```python
        self.LabelTexteDroite.setText(texte_aff_droite)
        self.LabelTexteCentre.setText(texte_aff_centre)
        self.LabelTexteGauche.setText(texte_aff_gauche)
        self.LabelTapeDroit.setText(texte_aff_basdroite)
```
###Méthode (slot) `togglePauseM`
Méthode permettant d'activer/désactiver la pause
```python
    @pyqtSlot()
    def togglePauseM(self):
```
Si le temps est fini, le bouton start/pause permet recommencer 
(méthode `recommencer`)
```python
        if self.jeton_temps_finiM:
            self.recommencer()
```
Si le temps n'est pas fini, et que c'est le premier lancement :  
```python
        elif self.premier_lancement_timer:
```
On désactive la pause (`jeton_pauseM`) et le drapeau de premier 
lancement (`premier_lancement_timer`)
```python
            self.premier_lancement_timer = False
            self.jeton_pauseM = False
```
Pour le premier caractère, on prend un temps arbitraire de 0,5 s
```python
            self.temps_score_precedant = time() - 0.5
```
On lance ensuite le timer pour la première fois ;  
```python
            self.Timer.start()
```
On change le texte du bouton start/pause ;  
On active les différents labels désactivés lors du lancement ;
Et on active le focus sur la boîte de texte
```python
            self.BoutonStartPause.setText(u"Pause")
            self.LabelTexteDroite.setEnabled(True)
            self.LabelTexteCentre.setEnabled(True)
            self.LabelTexteGauche.setEnabled(True)
            self.LabelTapeDroit.setEnabled(True)
            self.EntryTapeCentre.setFocus()
            self.LabelTapeFleche.setEnabled(True)
```
Si le temps n'est pas fini et que ce n'est pas le premier 
lancement :
```python
        else:
```
Si `jeton_pause_M` vaut `False` (pas de pause), on lance la 
pause (méthode `pauseM`)
```python
            if not self.jeton_pauseM:
                self.pauseM()
```
Sinon (pause active), on désactive la pause (méthode 
`reprendreM`)
```python
            elif self.jeton_pauseM:
                self.reprendreM()
```
Méthode `pauseM`
Méthode permettant de mettre en pause le GUI
```python
    def pauseM(self):
```
On appelle la méthode `pauseT` du timer pour le mettre en pause
```python
        self.Timer.pauseT()
```
On change le texte du bouton start/pause et on active la pause en 
passant `jeton_pauseM` à `True`
```python
        self.BoutonStartPause.setText(u"Reprendre")
        self.jeton_pauseM = True
```
On désactive ensuite les différents labels en gardant le focus sur 
la boîte de texte
```python
        self.LabelTexteDroite.setEnabled(False)
        self.LabelTexteCentre.setEnabled(False)
        self.LabelTexteGauche.setEnabled(False)
        self.LabelTapeDroit.setEnabled(False)
        self.LabelTapeFleche.setEnabled(False)
        self.EntryTapeCentre.setFocus()
```
Enfin, on récupère la couleur actuelle des flèches que l'on 
sauvegarde, on on met les flèches en couleur par défaut (noir)
```python
        self.couleur_backup = self.LabelTapeFleche.styleSheet()
        self.LabelTapeFleche.setStyleSheet("")
```
###Méthode `reprendreM`
Méthode permettant de reprendre après une pause du GUI
```python
    def reprendreM(self):
```
On appelle la méthode `reprendreT` du timer pour enlever la pause 
du timer
```python
        self.Timer.reprendreT()
```
On change le texte du bouton start/pause et on désactive la pause en 
passant `jeton_pauseM` à `False`
```python
        self.BoutonStartPause.setText(u"Pause")
        self.jeton_pauseM = False
```
On réactive les labels précédemments désactivés durant la pause en 
gardant le focus sur la boîte de texte
```python
        self.LabelTexteDroite.setEnabled(True)
        self.LabelTexteCentre.setEnabled(True)
        self.LabelTexteGauche.setEnabled(True)
        self.LabelTapeDroit.setEnabled(True)
        self.EntryTapeCentre.setFocus()
        self.LabelTapeFleche.setEnabled(True)
```
On remet la couleur que les flèches avaient lors de la mise en pause 
grâce à la valeur sauvegardée
```python
        self.LabelTapeFleche.setStyleSheet(self.couleur_backup)
```
###Méthode (slot) `quitterM`
Méthode permettant de quitter proprement le programme en fermant d'abord 
le timer
```python
    @pyqtSlot()
    def quitterM(self):
```
On appelle la méthode `quitterT` du timer pour le fermer, et on 
attend qu'il se ferme
```python
        self.Timer.quitterT()
        self.Timer.wait()
        self.termine.emit(self.recommencerV)
```
Enfin, on ferme le programme
```python
        self.close()
```
###Méthode (slot) `temps_change`
Méthode permettant de mettre à jour le temps affiché lors de l'émission 
du signal `temps_change_signal`
```python
    @pyqtSlot(float)
    def temps_change(self, temps_restant):
```
On récupère la valeur de `temps_restant` portée par le signal qui 
appel ce slot (cette méthode)
```python
        self.temps_restant = temps_restant
```
On met alors à jour l'affichage du temps restant et la barre 
d'avancement
```python
        self.LabelRestantV.setText(unicode(
                                   "{} / {}"
                                   .format(round(self.temps_restant, 1),
                                           round(self.temps_choisi, 1))))
        self.BarreAvancement.setValue(int(round((self.temps_restant /
                                                 self.temps_choisi) * 100, 0)))
```
###Méthode (slot) `temps_fini`
Méthode appelée lorsque le temps est fini et permettant de paramètrer le 
GUI pour un enventuel nouveau lancement (si l'utilisateur recommence)
```python
    @pyqtSlot()
    def temps_fini(self):
```
On désactive tous les labels et on remet la couleur des flèches par 
défaut (noir)
```python
        print("Temps fini")
        self.LabelTexteDroite.setEnabled(False)
        self.LabelTexteCentre.setEnabled(False)
        self.LabelTexteGauche.setEnabled(False)
        self.LabelTapeDroit.setEnabled(False)
        self.EntryTapeCentre.setEnabled(False)
        self.LabelTapeFleche.setStyleSheet("")
        self.LabelTapeFleche.setEnabled(False)
```
On met la variable `jeton_temps_finiM` à `True` et on appelle la 
méthode `setUpRecommencer` pour repréparer le GUI pour un nouveau 
lancement
```python
        self.jeton_temps_finiM = True
        self.setUpRecommencer()

        print("Appel gerer score")
        self.gererScore()
```
###Méthode `setUpRecommencer`
Méthode permettant de reparamétrer le GUI pour un nouveau lancement
```python
    def setUpRecommencer(self):
```
On change le texte du bouton start/pause
```python
        self.BoutonStartPause.setText(u"Recommencer")
```
###Méthode `recommencer`
Méthode permettant de recommencer
```python
    def recommencer(self):
```
On passe la valeur de `recommencerV` à `True`  
On appelle ensuite la méthode `quitterM` permettant de quitter
```python
        self.recommencerV = True
        self.quitterM()
```
###Méthode `genererStats`
Méthode permettant de générer les statistiques
```python
    def genererStats(self):
```
On appelle les différentes méthodes en charge des statistiques
```python
        self.temps_ecoule = self.temps_choisi - self.temps_restant
        if not self.temps_ecoule == 0:
            self.compterMots()
            self.compterCar()
            self.compterJusteErreur()
            self.compterScore()
```
###Méthode `compterMots`
Méthode permettant de compter le nombre de mots tapés et de calculer 
ensuite le temps moyen mis pour taper un mot (`mots_min`)
```python
    def compterMots(self):
```
On calcule le nombre de mots tapés à partir de la valeur de `texte_d`
```python
        texte_mod = self.texte_d.replace("'", " ")
        nombre_mots = len((texte_mod).split(" ")) - 1
```
On définit le nombre de mots tapés comme étant supérieur à 1
```python
        if nombre_mots > self.nombre_mots_precedant:
```
On change l'ancienne valeur de `nombre_mots_precedant`
```python
            self.nombre_mots_precedant = nombre_mots
```
On calcule le nombre de mots tapés par minite et on l'affiche 
dans l'interface
```python
            self.mots_min = nombre_mots / (self.temps_ecoule / 60.0)
            self.LabelMotsMinV.setText(unicode(str(round(self.mots_min, 1))))
```
###Méthode `compterCar`
Méthode permettant de compter et d'afficher le nombre de caractères 
tapés à la minute (`car_min`)
```python
    def compterCar(self):
```
On calcule le nombre de caractères tapés depuis la valeur `texte_d`
```python
        nombre_car = len(self.texte_d)
        self.car_min = nombre_car / (self.temps_ecoule / 60.0)
```
On affiche le nombre de caractères tapés par minute, arrondi à 
l'entier le plus proche
```python
        self.LabelCarMinV.setText(unicode(str(int(round(self.car_min, 0)))))
```
###Méthode `compterJusteErreur`
Méthode permettant de calculer et d'afficher dans les barres 
horizontales le pourcentage de caractères justes et faux (réussite et 
erreurs)
```python
    def compterJusteErreur(self):
```
On définit la somme, supérieure à 1, des caractères justes et faux
```python
        somme = self.car_justes + self.car_faux
        if somme == 0:
            somme = 1
```
On calcule les ratios de caractères justes et faux en fonction de la 
somme calculée précedemment
```python
        self.reussite = self.car_justes / somme
        self.erreurs = self.car_faux / somme
```
Enfin, on affiche dans l'interface (sur les barres horizontales) 
les deux valeurs que l'on vient de calculer
```python
        self.BarreReussite.setValue(round(self.reussite * 100, 0))
        self.BarreErreurs.setValue(round(self.erreurs * 100, 0))
```
###Méthode `compterScore`
Méthode permettant de calculer le score selon la nouvelle formule  
*À détailler*
```python
    def compterScore(self):
        if self.dernier_juste:
```
On recherche le type de caractères
```python
            if self.der_car_T == " ":
                coeff = 0.4
            elif re.match(r"[a-z]", self.der_car_T):
                coeff = 0.5
            elif re.match(r"[A-Z]", self.der_car_T):
                coeff = 0.8
            elif re.match(r"[²&é\"'(-è_çà)=,;:!<]", self.der_car_T):
                coeff = 1
            elif re.match(r"[0-9°+?./§>]", self.der_car_T):
                coeff = 1.2
            else:
                coeff = 1.6
```
On calcule le temps et les différents facteurs
```python
            temps_score = time()
            temps_ecoule_l = temps_score - self.temps_score_precedant
            inv_temps_pour_car = 1 / (temps_ecoule_l)
            self.temps_score_precedant = temps_score
            nombre_erreur_pour_car = self.car_faux -\
                self.car_faux_precedant
            self.car_faux_precedant = self.car_faux
            inv_de_err_plus_un = 1 / (nombre_erreur_pour_car + 1)
            ln_tps_plus_C_div_tps = (log(self.temps_choisi) +
                                     self.C_TEMPS) / self.temps_choisi
```
On calcule le score final et on l'affiche
```python
            score_car = inv_temps_pour_car * inv_de_err_plus_un * \
                ln_tps_plus_C_div_tps * coeff * self.C_SCORE * self.coeff_pre
            self.score += score_car
            self.LabelScoreV.setText(unicode(str(int(round(self.score,
                                                           0)))))

    def gererScore(self):
        print("Début Gérer score")
        print("Gestion temps")
        dh = localtime()
        AAAA = str(dh[0])
        print("Année")
        while len(AAAA) < 4:
            AAAA = "0" + AAAA
        MM = str(dh[1])
        print("Mois")
        while len(MM) < 2:
            MM = "0" + MM
        print("jour")
        JJ = str(dh[2])
        while len(JJ) < 2:
            JJ = "0" + JJ
        print("Heure")
        hh = str(dh[3])
        while len(hh) < 2:
            hh = "0" + hh
        print("minute")
        mm = str(dh[4])
        while len(mm) < 2:
            mm = "0" + mm
        print("seconde")
        ss = str(dh[5])
        while len(ss) < 2:
            ss = "0" + ss
        print("Fin gestion temps debut gestion mode")
        mds = self.mode_texte.split("::")
        if mds[0] == "expl":
            mode_texte_enh = "Texte d'exemple {}"\
                .format(mds[1])
        elif mds[0] == "syll":
            mode_texte_enh = "Mots avec la syllabe -{}"\
                .format(mds[1])
        elif mds[0] == "mots_fr":
            mode_texte_enh = "Les {} mots les plus courants"\
                .format(mds[1])
        elif mds[0] == "perso":
            if mds[1] == "nom":
                mode_texte_enh = "Texte personnalisé : \"{}\""\
                    .format(mds[2][3:-3].split("/")[-1])
            elif mds[1] == "entier":
                mode_texte_enh = "Texte personnalisé : {}..."\
                    .format(mds[2][3:-3][:min(10, len(mds[2][3:-3]))])
        else:
            mode_texte_enh = "Inconnu"
        print("Fin mode début dico")
        dico_score = {"pseudo": self.pseudo,
                      "score": int(round(self.score, 0)),
                      "cpm": round(self.car_min, 1),
                      "mpm": round(self.mots_min, 1),
                      "temps": int(self.temps_choisi),
                      "d_h": "{}-{}-{} {}:{}:{}".format(AAAA, MM, JJ, hh, mm,
                                                        ss),
                      "texte_mode": self.mode_texte,
                      "texte_t": self.texte_d.encode("utf-8"),
                      "texte_mode_enh": mode_texte_enh}
        print("--> Dico généré")
        self.stockerLocalScore(dico_score)
        print("--> Local Score fait")
        crypterScore.crypterScoreAttente(dico_score)
        print("--> En Attente Score fait")
        adresse = crypterScore.envoyerScoreAttente()
        print("--> Envoyer fait")
        self.affFenetreScore(dico_score, adresse)

    def stockerLocalScore(self, dico_score):
        dico_score_raccourci = {"pseudo": dico_score["pseudo"],
                                "score": dico_score["score"],
                                "cpm": dico_score["cpm"],
                                "mpm": dico_score["mpm"],
                                "temps": dico_score["temps"],
                                "d_h": dico_score["d_h"],
                                "texte_mode_enh": dico_score["texte_mode_enh"]}
        try:
            fichier_db = open("score/local_db.db", "rb")
            mon_pickler = pickle.Unpickler(fichier_db)
            try:
                liste = mon_pickler.load()
            except:
                liste = []
            finally:
                fichier_db.close()
        except:
            liste = []
        liste.append(dico_score_raccourci)
        liste = sorted(liste, key=lambda dico: dico["score"], reverse=True)
        fichier_db = open("score/local_db.db", "wb")
        mon_pickler = pickle.Pickler(fichier_db)
        mon_pickler.dump(liste)
        fichier_db.close()

    def termineScore(self):
        del self.Score
        self.show()

    def affFenetreScore(self, dico_score, adresse):
        print("INIT")
        self.Score = ScoreApplication(dico_score, adresse)
        print("Créée")
        self.Score.termine.connect(self.termineScore)
        print("Bind signal")
        self.Score.setWindowModality(Qt.ApplicationModal)
        print("Modal")
        self.hide()
        print("Module caché")
        self.Score.show()
        print("Affiché")
```
##Classe `ThreadTimer`
La classe `ThreadTimer`, héritée de `QThread`, permet de lancer un timer en
thread d'arrière plan, qui fonctionne tout seul (standalone)  
On peut intéragir avec le timer grâce aux méthodes `pauseT`, `reprendreT` et
`quitterT`
```python
class ThreadTimer(QThread):
```
###En-tête de la classe
On créé ici les signaux `pyqtSignal` permettant d'intéragir avec le GUI
Ces signaux seront ensuite connectés au GUI avec la méthode `connect`
```python
    temps_fini_signal = pyqtSignal()
    temps_change_signal = pyqtSignal(float)
    finished = pyqtSignal()
```
###Méthode d'initialisation `__init__
Méthode permettant d'initialiser la classe
```python
    def __init__(self, temps_choisi=60):
```
On hérite de la méthode `__init__` de la classe parente (`QThread`)
```python
        QThread.__init__(self)
```
On créé les attributs de la classe
```python
        self.temps_choisi = temps_choisi
        self.temps_depart = 0.0
        self.temps_inter = 0.0
        self.temps_ecoule = 0.0
        self.temps_restant = 0.0
        self.jeton_quitter = False
        self.jeton_pause = True
        self.temps_debut_pause = 0.0
        self.temps_fin_pause = 0.0
```
###Méthode principale `run`  
Cette méthode correspond au corps du thread, qui est appelée lors du
`start()`, et dont la fin correspond à la fin de l'execution du thread
```python
    def run(self):
```
On prend le temps lors du lancement et on désactive la pause
```python
        self.temps_depart = time()
        self.jeton_pause = False
```
Tant que `jeton_quitter` est `False` (tant que l'on ne veut pas
quitter)  
On calcule le temps restant
```python
        while not self.jeton_quitter:
            self.temps_inter = time()
            self.temps_ecoule = self.temps_inter - self.temps_depart
            self.temps_restant = self.temps_choisi - self.temps_ecoule
```
Si il est négatif, on le met à `0`, on met une dernière fois à
jour le temps (signal `temps_change`), et on envoie un signal
pour dire que le temps est fini (signal `temps_fini`)  
Enfin, on termine la méthode (`return`)
```python
            if self.temps_restant <= 0.0:
                self.temps_restant = 0.0
                self.temps_change_signal.emit(self.temps_restant)
                self.temps_fini_signal.emit()
                return
```
Sinon, on met à jour le temps (signal `temps_change`), et on
fait hiberner le programme pendant `0,01` s
```python
            else:
                self.temps_change_signal.emit(self.temps_restant)
                sleep(0.01)
```
Si la pause est activée, on prend le temps de début de pause  
Ensuite, tant que la pause est activée et que le timer ne doit 
pas être quitté, le programme hiberne par pas de 0,01 s
```python
            if self.jeton_pause:
                self.temps_debut_pause = time()
                while self.jeton_pause and not self.jeton_quitter:
                    sleep(0.01)
```
Quand on sort de la boucle (pause terminée), on prend le
temps de fin de pause, on calcule le temps passé en pause,
et on ajoute cette durée au temps de lancement
(`temps_depart`)
```python
                self.temps_fin_pause = time()
                self.temps_pause_ecoule = (self.temps_fin_pause -
                                           self.temps_debut_pause)
                self.temps_depart += self.temps_pause_ecoule
```
Quand la boucle est cassée (quand `jeton_quitter` vaut `True`), on
émet un signale `finished` (utile pour la destruction au bon moment
 du thread)
```python
        self.finished.emit()
```
###Méthode de pause `pauseT`  
Cette méthode permet de mettre en pause le thread, en modifiant la
valeur de l'attribut `jeton_pause` de `False` à `True`
```python
    def pauseT(self):
        self.jeton_pause = True
```
###Méthode de pause `reprendreT`  
Cette méthode permet de reprendre le thread après une pause, en
modifiant la valeur de l'attribut `jeton_pause` de `True` à `False`
```python
    def reprendreT(self):
        self.jeton_pause = False
```
###Méthode permettant de quitter le timer `quitterT`  
Cette méthode permet de quitter le thread en modifiant la valeur de
l'attribut `jeton_quitter` de `False` à `True`  
Cela casse la boucle principale de la méthode `run` du thread
```python
    def quitterT(self):
        self.jeton_quitter = True
```
##Classe `ScoreApplication`
Cette classe hérite des classes `QWidget` et `Ui_Score` et permet la 
création du GUI et sa gestion  
Cette classe contient la majeure partie du programme de la fenêtre des 
scores  
Elle est directement issue de *Qt* et (et donc `PyQt`)
```python
class ScoreApplication(QWidget, Ui_Score):
    termine = pyqtSignal()
```
###Méthode d'initialisation `__init__`
Méthode permettant d'initialiser la classe
```python
    def __init__(self, dico_score, parent=None):
```
On hérite de la méthode `__init__` des classes parentes
```python
        super(ScoreApplication, self).__init__(parent)
```
On initialise les widgets décris dans le fichier auxiliaire 
`ui_score.py` créé avec *Qt Creator* et `PyQt`
```python
        self.setupUi(self)
```
On définit les attributs de la classe en fonction des paramtères du 
Constructeur
```python
        self.dico_score = dico_score
```
On affiche le logo dans la zone prévue
```python
        self.LabelIcone.setPixmap(QPixmap(os.getcwd() + "/img/logo3.png"))
```
On connecte les boutons à leur slot respectif
```python
        self.BoutonQuitter.clicked.connect(self.quitter)
        self.BoutonScoresLigne.clicked.connect(self.ouvrirPageScore)
```
On remplit les champs en fonction du `dico_score` passé en paramètre
```python
        self.LabelScoreV.setText(unicode(str(self.dico_score["score"])))
        self.LabelMPMV.setText(unicode(str(self.dico_score["mpm"])))
        self.LabelCPMV.setText(unicode(str(self.dico_score["cpm"])))
```
On appelle la méthode rang pour déterminer le rang en fonction du 
score, puis on l'affiche
```python
        rang = self.determinerRang(self.dico_score["score"])
        self.LabelRangV.setText(unicode(rang))
```
On appelle la méthode pour générer la page de score à partir de la 
DB locale, puis on l'affiche
```python
        self.genererHTMLDB(self.dico_score)
        self.ViewScore.load(QUrl("file:///" + os.getcwd() + "/score/db.html"))
        self.ViewScore.show()
```
On enlève le focus du bouton quitter pour ne pas que `<Space>` 
quitte la fenêtre
```python
        self.LabelScoreV.setFocus()
```
###Méthode spéciale `keyPressEvent`
Méthode prenant en paramètres `event` et permettant de gérer les actions 
au clavier
```python
    def keyPressEvent(self, event):
```
Si l'événement est une pression de touche
```python
        if type(event) == QKeyEvent:
```
Si la touche pressée est `<Escape>` ou `<Return>`
```python
            if event.key() == Qt.Key_Escape or event.key() == Qt.Key_Return:
```
On quitte la fenêtre
```python
                self.quitter()
```
###Méthode `determinerRang`
Méthode permettant de déterminer le rang du joueur en fonction du score 
passé en paramètres
```python
    def determinerRang(self, score):
```
On regarde dans quelle tranche se trouve le joueur
```python
        if score > 5000:
            rang = "Big-Bang"
        elif score <= 5000 and score > 3000:
            rang = "Trou-Noir"
        elif score <= 3000 and score > 2000:
            rang = "SuperNova"
        elif score <= 2000 and score > 1500:
            rang = "Dieu"
        elif score <= 1500 and score > 1000:
            rang = "Demi-Dieu"
        elif score <= 1000 and score > 750:
            rang = "Champion"
        elif score <= 750 and score > 500:
            rang = "Archer"
        elif score <= 500 and score > 250:
            rang = "Guerrier"
        elif score <= 250 and score > 100:
            rang = "Novice"
        else:
            rang = "Newbie"
```
Et on retourne le rang correspondant
```python
        return rang
```
###Méthode (slot) `ouvrirPageScore`
Méthode appelée lorsque l'on appuie sur le bouton `BoutonScoresLigne`, 
et permettant d'afficher la page internet affichant les scores en lignes
```python
    @pyqtSlot()
    def ouvrirPageScore(self):
```
On encode en hexadecimal les pseudo, date et heure du score qui 
vient d'être réalisé
```python
        pseudo_cur = binascii.b2a_hex(self.dico_score["pseudo"])
        date_cur = binascii.b2a_hex(self.dico_score["date"])
        heure_cur = binascii.b2a_hex(self.dico_score["heure"])
```
On définit l'adresse en fonction des pseudo, date et heure en hex
```python
        adr = ("http://tbagrel1.pythonanywhere.com/app1/viewScores" +
               "?score={}&date={}&heure={}").format(pseudo_cur,
                                                    date_cur,
                                                    heure_cur)
```
On affiche la page internet correspondante
```python
        webbrowser.open(adr)
```
###Méthode `genererHTMLDB`
Méthode générant la page HTML des scores à partir de la DB locale
```python
    def genererHTMLDB(self, dico_score):
```
On récupère les pseudo et score courants pour afficher en rouge la 
ligne correspondant à la partie en cours
```python
        pseudo_cur = dico_score["pseudo"]
        score_cur = dico_score["score"]
```
On définit le code HTML de la page
```python
        c = ""
        c +=\
            """<html lang="fr">
    <head>
        <meta charset="UTF-8" />
        <style>
            *
            {
                font-family: "Comic sans MS", Verdana, sans-serif;
                font-size: 14px;
            }

            #normal
            {

            }

            #best
            {
                background-color: yellow;
            }

            #self
            {
                background-color: red;
            }

            #cat
            {
                background-color: gray;
            }
        </style>

        <title>Scores IGGF</title>
    </head>

    <body>
"""
        c +=\
            """        <table>
"""
```
On ouvre la DB locale  
La DB locale est forcément définie car elle vient d'être créée si 
elle n'existait pas lors de la fin de la partie
```python
        fichier_db = open("score/local_db.db", "rb")
```
On récupère le contenu sous forme d'une liste de dictionnaires grâce 
à un pickler
```python
        mon_pickler = pickle.Unpickler(fichier_db)
        liste = mon_pickler.load()
        fichier_db.close()
```
On gère le type de ligne
```python
        pas_encore_trouve_best = True
```
Pour chaque élément dans la liste
```python
        for elt in liste:
            type_ligne = "normal"
```
Si l'élément commence par un `"#"`, alors la ligne correspond à 
une catégorie 
```python
            if str(elt["pseudo"])[0] == "#":
                type_ligne = "cat"
```
On prend le premier score n'étant pas une catégorie, que l'on 
définit comme le record
```python
            elif pas_encore_trouve_best:
                type_ligne = "best"
                pas_encore_trouve_best = False
```
Sinon si le score et le pseudo de la ligne correspondent à ceux 
de la partie qui vient d'être faîte, on définit le score comme 
le sien
```python
            elif (str(elt["pseudo"]) == str(pseudo_cur) and
                  str(elt["score"]) == str(score_cur)):
                type_ligne = "self"
```
Sinon, la ligne est du type normal
```python
            else:
                type_ligne = "normal"
```
On ajoute alors au fichier HTML la ligne correspondante dans le 
tableau
```python
            nl = """            <tr id={}>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
"""\
                .format(str(type_ligne),
                        str(elt["pseudo"]),
                        str(elt["score"]),
                        str(elt["cpm"]),
                        str(elt["mpm"]),
                        str(elt["temps"]),
                        str(elt["d_h"]),
                        str(elt["texte_mode_enh"]))
            c += nl
```
Enfin, on finit d'écrire le fichier HTML
```python
        c += """        </table>
    </body>
</html>"""
```
On écrit alors le code HTML dans un fichier
```python
        fichier_html = open("score/fichier_html.html", "w")
        fichier_html.write(c)
        fichier_html.close()
```
Et on affiche le code HTML dans la zone prévue
```python
        self.ViewScore.setHtml(c.decode("utf-8"))
```
###Méthode (slot) `quitter`
Méthode permettant de quitter la fenêtre des scores
```python
    @pyqtSlot()
    def quitter(self):
```
On émet le signal `termine`
```python
        self.termine.emit()
```
On ferme la fenêtre
```python
        self.close()
```
#Programme principal

##Fonction `main`
Fonction ne prenant pas d'arguments et permettant de créer l'interface et de 
la lancer
```python
def main():
```
On créé une application *Qt* `Qapplication`, pour porter notre GUI
```python
    app = QApplication(sys.argv)
```
On créé notre GUI comme étant une instance de la classe 
`MenuApplication` décrite plus haut
```python
    myapp = MenuApplication()
    # #.On affiche notre GUI et on connecte sa fermeture à la fermeture du 
    # #.programmme
    myapp.affFenetreBVN()
    app.exec_()

    del myapp
    del app
```
##Test de lancement standalone
Test permettant de lancer le programme si il est exécuté directement tout 
seul, sans import
```python
if __name__ == "__main__":
```
On appelle la fonction `main` définit plus haut
```python
    main()
```
