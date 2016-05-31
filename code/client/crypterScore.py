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

    #.###Méthode principale `run`
    #.Cette méthode correspond au corps du thread, qui est appelée lors du 
    #.`start()`, et dont la fin correspond à la fin de l'exécution du thread
    def run(self):

        #.ON ENVOIE LES SCORES EN ATTENTE
        test_co = urllib\
            .urlopen("http://tbagrel1.pythonanywhere.com/app1/sendScore")
        if test_co.read() == "OK":
            try:
                fichier_score = open("score/en_attente.db", "r")
                scores_a_envoyer_brut = fichier_score.read()
                fichier_score.close()
            except:
                scores_a_envoyer_brut = ""

            fichier_erreur = open("score/erreur.db", "a")

            liste_score = [elt for elt in
                           scores_a_envoyer_brut.split("||||||||||") if elt and
                           elt != "\n"]
            if liste_score:
                for elt in liste_score:
                    #.`elt` correspond au score envoyé
                    retour = urllib.\
                        ulropen("http://tbagrel1.pythonanywhere.com/app1/" +
                                "sendScore?score={}".format(elt)).read()
                    if retour == "OK" or\
                        retour == "Erreur : Hexadecimal Decode" or\
                        retour == "Erreur : Decrypt AES" or\
                            retour == "Erreur : Depickler":
                            pass
                    else:
                        fichier_erreur.append(elt + "||||||||||")

            fichier_erreur.close()

        #.ON EFFACE LES SCORES EN ATTENTE

        fichier_score = open("score/en_attente.db", "w")
        fichier_score.write("")
        fichier_score.close()

        #.ON RÉCUPÈRE LA NOUVELLE DB

        db = urllib.urlopen("http://tbagrel1.pythonanywhere.com/app1/getDB")
        db = db.read()
        if db and db != "\n":
            print(db)
            db = binascii.a2b_hex(db)
            print(db)
            fichier_temp = open("score/temp.tmp", "w")
            fichier_temp.write(db)
            fichier_temp.close()
            fichier_temp = open("score/temp.tmp", "r")
            mon_pickler = pickle.Unpickler(fichier_temp)
            db = mon_pickler.load()
            fichier_temp.close()
            os.remove("score/temp.tmp")
        if db and db != "\n":
            fichier_db = open("score/local_db.db", "w")
            mon_pickler = pickle.Pickler(fichier_db)
            mon_pickler.dump(db)
            fichier_db.close()

        #.On émet le signal de fin
        self.finished.emit()

#.##Déclaration des fonctions

#.##Fonction `crypterScoreAttente`
#.Fonction permettant de crypter et d'ajouter un score au fichier 
#.`en_attente.txt`
def crypterScoreAttente(dico_score):
    #.On créé l'encodeur avec le mot de passe et le vecteur d'initialisation 
    #.choisi
    encodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")
    #.On récupère la checksum du fichier qui envoie le score
    checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
    #.On créé une liste contenant la checksum ainsi que le dictionnaire de 
    #.score passé en argument
    liste = [checksum, dico_score]
    #.On ouvre le fichier temporaire pour pickle la liste
    fichier_temp = open("score/temp.tmp", "w")
    mon_pickler = pickle.Pickler(fichier_temp)
    mon_pickler.dump(liste)
    fichier_temp.close()
    #.On lit le fichier et on récupère la chaîne correspondant à la liste 
    #.picklée
    fichier_temp = open("score/temp.tmp", "r")
    texte = fichier_temp.read()
    fichier_temp.close()
    #.Une fois fini, on supprime le fichier temporaire
    os.remove("score/temp.tmp")

    #.On ajoute au texte récupéré des caractères `"\0"` pour que la longueur 
    #.de la chaîne soit un multiple de 16
    texte += "\0" * (16 - (len(texte) % 16))

    #.On envrypte le texte et on le code en hexadécimal
    texte_crypte = binascii.b2a_hex(encodeur.encrypt(texte))
    #.On l'ajoute au fichier de scores en attente
    fichier_score_attente = open("score/en_attente.db", "a")
    fichier_score_attente.write(texte_crypte + "||||||||||")
    fichier_score_attente.close()

#.#Programme principal

#.##Test de lancement standalone
#.Test permettant de lancer le programme si il est exécuté directement tout 
#.seul, sans import
if __name__ == "__main__":
    #.On ne fait rien
    pass
