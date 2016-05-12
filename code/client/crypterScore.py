#!/usr/bin/python2
# -*- coding: utf-8 -*

# Import des modules

import socket
import sys
import pickle
import os
import hashlib
import base64
from Crypto.Cipher import AES
from multiprocessing import Process, Pipe

class TimeoutProcess():
    def __init__(self, fonction, timeout):
        self.fonction = fonction
        self.timeout = timeout

    def __call__(self, *args, **kwargs):
        def process_exec_nt(pipe, fonction, args, kwargs):
            valeur_retournee = fonction(*args, **kwargs)
            pipe.send(valeur_retournee)

        pipe_parent, pipe_enfant = Pipe()
        process_exec_t = Process(target=process_exec_nt, args=(pipe_enfant,
                                                               self.fonction,
                                                               args,
                                                               kwargs))
        process_exec_t.start()
        process_exec_t.join(self.timeout)

        if process_exec_t.is_alive():
            process_exec_t.terminate()
            return None
        else:
            return pipe_parent.recv()

def crypterScoreAttente(dico_score):

    encodeur = AES.new('mot_de_passe_16o', AES.MODE_CBC, "vecteur_init_16o")

    checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
    liste = [checksum, dico_score]

    fichier_temp = open("score/temp.tmp", "w")
    mon_pickler = pickle.Pickler(fichier_temp)
    mon_pickler.dump(liste)
    fichier_temp.close()

    fichier_temp = open("score/temp.tmp", "r")
    texte = fichier_temp.read()
    fichier_temp.close()
    os.remove("score/temp.tmp")

    texte += "\0" * (16 - (len(texte) % 16))

    texte_crypte = base64.encodestring(encodeur.encrypt(texte))
    fichier_score_attente = open("score/en_attente.db", "a")
    fichier_score_attente.write(texte_crypte + "||||||||||")
    fichier_score_attente.close()

def connection(adresse, port):
    try:
        client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_to_serv.connect((adresse, port))
        print("Réussi {}".format(adresse))
        client_to_serv.send("TEST\end")
        return adresse, port
    except:
        print("Raté {}".format(adresse))
        return None

def envoyerScoreAttente():

    adresse_port = TimeoutProcess(connection, 1)("pi-pc", 25565)
    if not adresse_port:
        adresse_port = TimeoutProcess(connection, 2)("bagrel.ddns.net", 25565)
    #.Si l'on a réussi à se connecter à l'une des adresses
    if adresse_port:
        client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_to_serv.connect((adresse_port[0], adresse_port[1]))
        client_to_serv.send("OTHER\end")
        #.On ouvre le fichier de scores cryptés en attente
        fichier_score = open("score/en_attente.db", "r")
        scores_a_envoyer = fichier_score.read()
        print(scores_a_envoyer)
        fichier_score.close()
        #.Si il y a des scores en attente, on les envoie, sinon on envoie une
        #.chaîne vide
        print("Envoi des scores...")
        if scores_a_envoyer and scores_a_envoyer != "\n":
            print("Il y a des nouveaux scores -> on les envoie")
            scores_a_envoyer += "\end"
            client_to_serv.send(scores_a_envoyer)
        else:
            print("Pas de nouveaux scores, on envoie une chaîne vide")
            client_to_serv.send("\end")

        print("Réception de la DB...")
        #.Le serveur va ajouter les scores dans la DB et renvoyer un tuple 
        #.contenant les codes d'erreurs ainsi que la nouvelle DB mise à jour
        msg_recu = ""
        msg_recu += client_to_serv.recv(1024)
        while msg_recu[-4:] != "\end":
            msg_recu += client_to_serv.recv(1024)
        msg_recu = msg_recu[:-4]
        print(msg_recu)
        #.On décode et dépickle le message reçu et on récupère les codes de 
        #.retour et la nouvelle DB
        print("Decodage de la DB...")
        retour = base64.decodestring(msg_recu)
        fichier_temp = open("temp.tmp", "wb")
        fichier_temp.write(retour)
        fichier_temp.close()
        fichier_temp = open("temp.tmp", "rb")
        mon_pickler = pickle.Unpickler(fichier_temp)
        retour = mon_pickler.load()
        fichier_temp.close()
        os.remove("temp.tmp")
        code_retour = retour[0]
        db = retour[1]
        print(code_retour)
        print(db)

        #.Si des scores nouveaux ont été envoyés, on a besoin de s'occuper des 
        #.codes d'erreurs
        print("Gestion des codes d'erreurs")
        if scores_a_envoyer and scores_a_envoyer != "\n":
            print("Nouveaux scores -> Erreurs ?")
            erreurs = []
            #.Pour chaque code d'erreur qui ne vaut pas `"OK"`
            for i in range(len(code_retour)):
                if code_retour[i] != "OK":
                    #.On ajoute le score correspondant à la liste des scores
                    #.qui contiennent les erreurs
                    erreurs.append(scores_a_envoyer[i])
            #.Si il y a eu des erreurs
            if erreurs:
                #.On sépare les différents scores qui ont été envoyés
                scores_a_envoyer = [elt for elt in
                                    scores_a_envoyer.split("||||||||||") if 
                                    elt and elt != "\n"]
                #.On essaye d'ouvrir le fichier des erreurs, et on récupère 
                #.les erreurs déjà inscrites, pour ne pas écrire plusieurs 
                #.fois les mêmes
                try:
                    fichier_erreur = open("score/erreur.db", "r")
                    erreurs_prec = [elt for elt in 
                                    fichier_erreur.read().split("||||||||||")
                                    if elt and elt != "\n"]
                    fichier_erreur.close()
                #.Si le fichier n'existe pas, on définit qu'il n'y a pas 
                #.encore d'erreurs enregistrées
                except:
                    erreurs_prec = []
                #.Pour chaque nouvelle erreur
                for erreur in erreurs:
                    #.Si elle n'est pas dans la liste des erreurs déjà 
                    #.enregistrées, on l'ajoute
                    if erreur in erreurs_prec:
                        pass
                    else:
                        erreurs_prec.append(erreur)
                #.On ouvre ensuite le fichier d'erreur en écriture et on écrit 
                #.la liste des erreurs
                fichier_erreur = open("score/erreur.db", "w")
                erreurs_prec = "||||||||||".join(erreurs_prec)
                if erreurs:
                    erreurs += "||||||||||"
                fichier_erreur.write(erreurs_prec)
                fichier_erreur.close()
        else:
            print("Pas de nouveaux scores -> Pas d'erreurs")

        print("Inscription de la nouvelle DB...")
        #.Si il n'y a pas eu d'erreur et qu'une nouvelle DB a bien été envoyée
        if db and db != "\n":
            print("Nouvelle DB récupérée")
            #.On écrit la nouvelle DB à la place de l'ancienne
            fichier_db = open("score/local_db.db", "wb")
            mon_pickler = pickle.Pickler(fichier_db)
            mon_pickler.dump(db)
            fichier_db.close()
        else:
            print("Pas de nouvelle DB")

        #.Enfin, on supprime les scores en attente puisqu'ils ont été soit 
        #.envoyés, validés et ajoutés à la DB soit placés dans le fichier 
        #.d'erreur pour pouvoir les récupérer en cas d'erreur non justifiée
        print("Suppression des scores en attente qui ont été envoyés...")
        fichier_score = open("score/en_attente.db", "w")
        fichier_score.write("")
        fichier_score.close()

        print("Envoi de la confirmation de réception...")
        #.On valide pour dire au serveur qu'on peut se déconnecter
        client_to_serv.send("OK\end")
    print(">>> Connection terminée")
envoyerScoreAttente()
