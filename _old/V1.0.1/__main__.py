# -*- coding:utf-8 -*

################################################################################
#                                                                              #
#                             --- FAST WRITING ---                             #
#                                                                              #
################################################################################

# Nom du programme :          Fast Writing
# Version :                   V1.0.1
# Affichage :                 Console (Terminal de 80 caractères)
# Auteur :                    Thomas BAGREL
# Adresse :                   tomsb07@gmail.com

# Import des modules
import time
import os
import random

# Ouverture de la liste de mots
ListeMotsBrut = open("ListeMots.txt", "r", encoding="iso-8859-1")
ListeMots = ListeMotsBrut.readlines()

# Boucle pour (re)jouer
Recommencer = True
while Recommencer == True:
    Compteur = 0
    TempsChoisi = int(input("Combien de secondes voulez-vous jouer ?\n"))
    DebutJeu = ""
    while DebutJeu != "o":
        DebutJeu = str(input("Entrez o pour commencer\n"))
    HeureDepart = time.time()
    while time.time() - HeureDepart < TempsChoisi:
        JetonMot = random.randint(0,197)
        MotChoisi = ListeMots[JetonMot]
        MotTape = ""
        ChaineValidation = []
        TopValidation = 0
        while TopValidation == 0:
            MotTape = str(input("Tapez le mot : "+MotChoisi))
            LongueurMotTape = len(MotTape)
            for i in range (1, int(LongueurMotTape + 1)):
                if MotTape[(i-1):i] == MotChoisi[(i-1):i]:
                    ChaineValidation.append(1)
                else:
                    ChaineValidation.append(0)
            if sum(ChaineValidation) == len(MotChoisi)-1 and len(MotTape) == \
 len(MotChoisi)-1:
                print("Bien joué !\n")
                Compteur = Compteur + 1
                TopValidation = 1
            else:
                print("Réessayez\n")
                TopValidation = 0
                ChaineValidation = []
    print("Temps écoulé !")
    print("Vous avez tapé "+str(Compteur)+" mots justes")
    print("------------------------")
    Choix = str(input("Voulez-vous recommencer ? (o/n)\n"))
    if Choix == "o":
        Recommencer = 1
    else:
        Recommencer = 0
ListeMotsBrut.close()
