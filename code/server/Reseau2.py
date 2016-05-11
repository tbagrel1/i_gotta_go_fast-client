#!/usr/bin/python2
# -*- coding: utf-8 -*

import pickle
import os
import base64
import socket
from Crypto.Cipher import AES
import MySQLdb

#.Définition des fonctions

def debase64(score):
    try:
        score = base64.decodestring(score)
        valid = "OK"
    except:
        score = ""
        valid = "Erreur : Base64 Decode"
    return (valid, score)

def decrypt(score):
    try:
        decodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC,
                           "vecteur_init_16o")
        score = decodeur.decrypt(score)
        while score[-1] == "\0":
            score = score[:-1]
        valid = "OK"
    except:
        score = ""
        valid = "Erreur : Decrypt AES"
    return (valid, score)

def depickle(score):
    try:
        doc_pick = open("temp.tmp", "wb")
        doc_pick.write(score)
        doc_pick.close()
        doc_pick = open("temp.tmp", "rb")
        mon_pickler = pickle.Unpickler(doc_pick)
        score = mon_pickler.load()
        doc_pick.close()
        os.remove("temp.tmp")
        valid = "OK"
    except:
        score = ""
        valid = "Erreur : Depickler"
    return (valid, score)

def dechecksum(score):
    if score[0] in liste_checksum:
        score = score[1]
        valid = "OK"
    else:
        score = ""
        valid = "Erreur : Checksum"
    return (valid, score)

def addDB(score):
    global DB
    DB_cur_score = DB.cursor()
    req = """INSERT INTO IGGF_V1 VALUES (id=NULL, pseudo=\"{}\", score={},
             cpm={}, mpm={}, temps={}, d_h=\"{}\", texte_mode=\"{}\",
             texte_t=\"{}\", texte_mode_enh=\"{}\");"""\
                .format(score["pseudo"],
                        score["score"],
                        score["cpm"],
                        score["mpm"],
                        score["temps"],
                        score["d_h"],
                        score["texte_mode"],
                        score["texte_t"],
                        score["texte_mode_enh"])
    print(req)
    try:
        DB_cur_score.execute(req)
        DB.commit()
        valid = "OK"
    except:
        DB.rollback()
        valid = "Erreur : Ajout DB"
    return valid

#.#Corps du programme

#.On récupère les checksums autorisées pour l'envoi des scores
fichier_checksum = open("checksum/checksum.db", "rb")
mon_pickler = pickle.Unpickler(fichier_checksum)
liste_checksum = mon_pickler.load()
fichier_checksum.close()
print(liste_checksum)

#.Connection à la base de données
DB = MySQLdb.connect(host="localhost", user="root", passwd="pipc54", db="IGGF")

#.On lance la connection réseau
serv_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#.On utilise le port `25565`
serv_co.bind(('', 25565))
#.On écoute un maximum d'une connection à la fois
serv_co.listen(1)

#.Tant que le serveur est en marche
while True:
    #.On accepte une connection et on récupère les informations de connection
    print("Acceptation de la connection...")
    (serv_to_client, infos_co) = serv_co.accept()
    print(infos_co)
    #.On reçoit les scores envoyés par le client
    print("Récupération du mode...")
    msg_recu = ""
    msg_recu += serv_to_client.recv(1024)
    while msg_recu[-4:] != "\end":
        print(msg_recu)
        msg_recu += serv_to_client.recv(1024)
    msg_recu = msg_recu[:-4]
    print(msg_recu)
    if msg_recu == "TEST":
        serv_to_client.close()
    else:
        print("Récupération des scores...")
        msg_recu = ""
        msg_recu += serv_to_client.recv(1024)
        while msg_recu[-4:] != "\end":
            print(msg_recu)
            msg_recu += serv_to_client.recv(1024)
        msg_recu = msg_recu[:-4]
        print(msg_recu)
        print("Traitement des nouveaux scores...")

        code_retour = []

        #.Si des nouveaux scores ont été envoyés
        if msg_recu and msg_recu != "\n":
            print("Nouveaux scores -> Traitement")

            #.On sépare les différents scores
            cs_plus_scores_crypt = [elt for elt in 
                                    msg_recu.split("||||||||||") if 
                                    elt and elt != "\n"]
            print(cs_plus_scores_crypt)

            #.Pour chaque score, on le fait passer par les différentes étapes 
            #.et on récupère le code d'erreur que l'on place dans `code_retour`
            for score in cs_plus_scores_crypt:
                print(score)
                valid = "OK"
                if valid == "OK":
                    (valid, score) = debase64(score)
                if valid == "OK":
                    (valid, score) = decrypt(score)
                if valid == "OK":
                    (valid, score) = depickle(score)
                if valid == "OK":
                    (valid, score) = dechecksum(score)
                if valid == "OK":
                    valid = addDB(score)

                code_retour.append(valid)

            print(code_retour)

        else:
            print("Pas de nouveaux scores -> Pas de traitement")

        #.Ensuite, on récupère la nouvelle DB mise à jour
        print("Récupération de la nouvelle DB...")
        DB_cur_getDB = DB.cursor()
        req = "SELECT * FROM IGGF_1 ORDER BY score DESC;"
        try:
            DB_cur_getDB.execute(req)
            tab = DB_cur_getDB.fetchall()
            db = []
            for ligne in tab:
                dico_score_simpl = {"pseudo": ligne[1],
                                    "score": ligne[2],
                                    "cpm": ligne[3],
                                    "mpm": ligne[4],
                                    "temps": ligne[5],
                                    "d_h": ligne[6],
                                    "texte_mode_enh": ligne[9]}
                db.append(dico_score_simpl)
            print("Nouvelle DB récupérée")
        except:
            db = ""
            print("Erreur -> Nouvelle DB vide")

        #.On prépare les codes de retour et la DB pour l'envoi...
        retour = (code_retour, db)

        print("Préparation de la DB et des codes retour pour l'envoi...")
        fichier_temp = open("temp.tmp", "wb")
        mon_pickler = pickle.Pickler(fichier_temp)
        mon_pickler.dump(retour)
        fichier_temp.close()
        fichier_temp = open("temp.tmp", "rb")
        retour = base64.encodestring(fichier_temp.read())
        fichier_temp.close()

        print("Envoi de la DB et des codes retour au client...")
        #.Et on envoie au client les codes de retours et la nouvelle DB
        retour = retour + "\end"
        serv_to_client.send(retour)

        print("En attente de la confirmation de bonne réception par le \
              client...")
        #.On attend ensuite la confirmation du client pour dire que le 
        #.traitement a bien été effectué
        msg_recu = ""
        msg_recu += serv_to_client.recv(1024)
        while msg_recu[-4:] != "\end":
            msg_recu += serv_to_client.recv(1024)
        msg_recu = msg_recu[:-4]
        print(msg_recu)
        print("Message reçu par le client et bien traité\nFemeture de la \
              connection...")
        #.Enfin, on ferme la connection avec le client
        serv_to_client.close()
        print(">>> Connection terminée")

#.On ferme la DB
DB.close()
