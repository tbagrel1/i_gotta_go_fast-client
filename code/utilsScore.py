#!/usr/bin/python2
# -*- coding: utf-8 -*
#ref_to_md

#.#Import des modules

#.##Imports `from`

#.Cryptage
from Crypto.Cipher import AES
#.Interface graphique `PyQt4`
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtNetwork

#.##Imports standards

#.Import des modules standards
import os
import sys
import pickle
import binascii
#.Import de `hashlib` pour la checksum
import hashlib
#.Import `urllib` pour lire les pages web
import urllib

#.#Déclaration des classes

#.##Fonction `ajouterScoreAttente`
#.Fonction permettant de crypter et d'ajouter un score au fichier 
#.`en_attente.txt`
def ajouterScoreAttente(dico_score):
    #.###Ajout à `score_A0.db` ou `score_A1.db`
    if dico_score["aff"]:
        try:
            fichier_score_A1 = open("score/scores_A1.db", "r")
            liste = pickle.load(fichier_score_A1)
            fichier_score_A1.close()
        except:
            liste = []
        liste.append(dico_score)
        fichier_score_A1 = open("score/scores_A1.db", "w")
        pickle.dump(liste, fichier_score_A1)
        fichier_score_A1.close()

    else:
        try:
            fichier_score_A0 = open("score/scores_A0.db", "r")
            liste = pickle.load(fichier_score_A0)
            fichier_score_A0.close()
        except:
            liste = []
        liste.append(dico_score)
        fichier_score_A0 = open("score/scores_A0.db", "w")
        pickle.dump(liste, fichier_score_A0)
        fichier_score_A0.close()

    #.###Ajout à `score_AX.db`
    #.On créé l'encodeur avec le mot de passe et le vecteur d'initialisation 
    #.choisi
    encodeur = AES.new("Wvab2rFaKiCNP5W4", AES.MODE_CBC, "PFaP61MX9pax9MmB")
    #.On récupère la checksum du fichier qui envoie le score
    checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
    #.On créé une liste contenant la checksum ainsi que le dictionnaire de 
    #.score passé en argument
    check_dico = [checksum, dico_score]
    #.On pickle la liste
    texte = pickle.dumps(check_dico)

    #.On ajoute au texte récupéré des caractères `"\0"` pour que la longueur 
    #.de la chaîne soit un multiple de 16
    texte += "\0" * (16 - (len(texte) % 16))

    #.On encrypte le texte et on le code en hexadécimal
    texte = binascii.b2a_hex(encodeur.encrypt(texte))
    #.On l'ajoute au fichier de scores en attente
    try:
        fichier_score_AX = open("score/score_AX.db", "r")
        liste = pickle.load(fichier_score_AX)
        fichier_score_AX.close()
    except:
        liste = []
    liste.append(texte)
    fichier_score_AX = open("score/score_AX.db", "w")
    pickle.dump(liste, fichier_score_AX)
    fichier_score_AX.close()

#.##Classe `ThreadSyncDB`
#.La classe `ThreadSyncDB`, héritée de `QThread`, permet de synchroniser la DB 
#.locale avec la DB online en processus d'arrière plan, qui fonctionne seul  
#.Le `ThreadSyncDB` communique avec le programme principal avec les signaux
class ThreadSyncDB(QThread):
    finished = pyqtSignal()

    #.###Méthode d'initialisation `__init__`
    #.Méthode permettant d'initialiser la classe
    def __init__(self):
        #.On hérite de la méthode `__init__` de la classe parente (`QThread`)
        QThread.__init__(self)
        self.debug = True

    #.###Méthode principale `run`
    #.Cette méthode correspond au corps du thread, qui est appelée lors du 
    #.`start()`, et dont la fin correspond à la fin de l'exécution du thread
    def run(self):

        # try:
        #     self.print_d("try")
        #     checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
        #     self.print_d(checksum)
        #     checksum = binascii.b2a_hex(checksum)
        #     self.print_d(checksum)
        #     self.print_d(binascii.b2a_hex("90bbbcaa5a836045c40a064ee55b75fb"))
        #     test_co = urllib.urlopen("http://tbagrel1.pythonanywhere.com/" +
        #                              "app1/testConnection?checksum={}"
        #                              .format(checksum)).read()
        #     self.print_d(test_co)
        #     if test_co != "OK":
        #         raise ChecksumError
        # except:
        #     test_co = "ERROR"

        # self.print_d(test_co)

        test_co = "OK"

        if test_co == "OK":
            try:
                fichier_score_AX = open("score/score_AX.db", "r")
                liste_score_envoyer = pickle.load(fichier_score_AX)
                fichier_score_AX.close()
            except:
                liste_score_envoyer = []

            erreur = []
            if liste_score_envoyer:
                self.print_d("Un ou plusieurs scores à envoyer")
                for elt in liste_score_envoyer:
                    #.`elt` correspond au score envoyé
                    try:
                        retour = urllib.urlopen("http://tbagrel1.python" + 
                                                "anywhere.com/app1/send" + 
                                                "Score?score={}"
                                                .format(elt)).read()
                        self.print_d(retour)
                        if retour != "OK":
                            self.print_d(retour)
                            raise Exception(retour)
                    except Exception as e:
                        retour = e.args[0]
                        if retour != "Erreur : Hexadecimal Decode" and retour \
                                != "Erreur : Decrypt AES" and retour != \
                                "Erreur : Depickler" and retour != \
                                "Erreur : Checksum":
                            erreur.append(elt)
                            self.print_d("Erreur inconnue durant l'envoi")
            else:
                self.print_d("Aucun score à envoyer")

            #.On efface les scores en attente
            try:
                os.remove("score/score_AX.db")
            except:
                self.print_d("Pas d'effacement des scores !!!")

            if erreur:
                self.print_d("Une ou plusieurs erreurs à réécrire")
                fichier_score_AX = open("score/score_AX.db", "w")
                pickle.dump(erreur, fichier_score_AX)
                fichier_score_AX.close()

            #.On récupère la nouvelle DB

            try:
                db = urllib\
                    .urlopen("http://tbagrel1.pythonanywhere.com/app1/getDB")\
                    .read()
            except:
                db = None
            if db and db != "\n":
                self.print_d(db)
                db = binascii.a2b_hex(db)
                self.print_d(db)
                db = pickle.loads(db)
                self.print_d(db)
                fichier_score_A1 = open("score/scores_A1.db", "w")
                pickle.dump(db, fichier_score_A1)
                fichier_score_A1.close()

        #.On émet le signal de fin
        self.finished.emit()

    def print_d(self, texte):
        if self.debug:
            print(texte)

def main():
    pass

#.##Déclaration des fonctions

#.#Programme principal

#.##Test de lancement standalone
#.Test permettant de lancer le programme si il est exécuté directement tout 
#.seul, sans import
if __name__ == "__main__":
    main()
