#!/usr/bin/python2
# -*- coding: utf-8 -*

# .##Modules :
#.Import du module socket afin de communiquer avec le client qui lui envera
#.des informations sur les scores
import socket
#.Import du modules pickle qui permet de recuperer un objet python stocké sous
#.forme de texte adapté
import pickle
#.Import des modules pour la cryptographie
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# .##Format de données reçues par le serveur
#.On reçoit du client plusieurs chaînes de caractères correspondant à une
#.liste contenant le code de la fonction de cryptage, la checksum du fichier
#.qui appelle la fonction ainsi que le dictionnaire de score, le tout crypté

# .##Les fonctions :
#.On recupere une ligne "pickle" correspondant au score, la
#.fonctions permet de rendre lisible les données que l'on
#.recupere sous forme texte et les passer sous forme python
som_ref = (...,...,...)

def putdata(score):
    print(score)

def unpick(msg):
    doc_pick = open("pickle.txt", "wb")
    doc_pick.write(msg)
    doc_pick.close()
    try:
        a = pickle.load(open("pickle.txt", "rb"))
        doc_pick.close()
        #.On verifie si le checksum est dans la la liste de réference, nous 
        #.informant que c'est bien notre programme qui a envoyer les données
        if a[0] in som_ref:
            a = a[1]
            putdata(a)
    except:
        doc_pick.close()

#.Tout ce qui est dans ce bloc correspond au cryptage symétrique
#.On prépare la clé Fernet qui permet de crypter et de décrypter
#------------------------------------------------------------------------------
mot_de_passe = "                "
# cle_16o = os.urandom(16) --> Il faut que les deux parties utilisent la même
cle_16o = "                "

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=cle_16o,
                 iterations=100000,
                 backend=default_backend())
cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
cle_fernet = Fernet(cle)
#------------------------------------------------------------------------------

#.On lance le service de connection
serv_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#.On utilise le port `25565`
serv_co.bind(('', 25565))
#. On écoute un maximum d'une connection à la fois
serv_co.listen(1)

#.Tant que le serveur est en marche
while True:
    #.On accepte une connection et on récupère les informations de connection
    (serv_to_client, infos_co) = serv_co.accept()
    #.On affiche les informations de connection pour verifier qu'il n'y pas 
    #.de probleme avec celle-ci
    print(infos_co)
    #.On envoi un message au client pour dire qu'il est bien connecté
    serv_to_client.send("OK\end")
    #.On recoit la commande push ou pull du clien, on utilise la boucle while, 
    #.si la demande est trop longue (en cas de test d'attaque de la base de 
    #.donnée)
    msg_recu = ""
    while msg_recu[-4:] != "\end":
        msg_recu += serv_to_client.recv(1024)
    msg_recu = msg_recu[:-4]
    print(msg_recu)
    #.On regarde ce que veut demander le clien au serveur entre 
    #.push et pull, ici push
    if msg_recu == "PUSH":
        #.On previent que le mode push est bien actif, et qu'il peut envoyer 
        #.les données.
        serv_to_client.send("OK\end")
        #.On recoit le score du clien, comme on ne peut recevoir que 1024 
        #.carractère a la fois, on ajoute chaque 1024 carractère les un apres 
        #.les autres
        msg_recu = ""
        while msg_recu[-4:] != "\end":
            msg_recu += serv_to_client.recv(1024)
        msg_recu = msg_recu[:-4]
        print(msg_recu)
        #.On envoi un message au client pour dire que le score est bien arrivé
        serv_to_client.send("OK\end")
        serv_to_client.close()
        #.On met ce que l'on recoit dans on document en l'ecriant sur une seul 
        #.ligne, plus facile pour les interpréters après
        fichier = open("message_crypte.txt", "wb")
        fichier.write(msg_recu)
        fichier.close()
        #.On recupère la ligne en la decriptant 
        fichier = open("message_crypte.txt", "rb")
        msg_crypte = fichier.read()
        fichier.close()
        msg_decrypte = cle_fernet.decrypt(msg_crypte)
        #.Une fois le message decrypté on utilise la fonction unpick qui 
        #.transforme un chaine de carractere (si elle a été pickle avant) 
        #.sous forme de code python, tres pratique pour envoyer des partie de 
        #.code, ici en l'occurence on envoi les scores sous forme de dictionaire
        #.avec en plus deux clé permetant de verifier la provenance des données
        unpick(msg_decrypte)



        serv_to_client.send("OK\end")

    #.On regarde ce que veut demander le clien au serveur entre 
    #.push et pull, ici pull
    elif msg_recu == "PULL":
        #.On previent que le mode pul est bien actif, et qu'il peut se preparer 
        #.a recevoir les données de la database.
        serv_to_client.send("OK\end")
        #.On envoi la database au clien avec un \end a la fin pour lui signaler 
        #.quand l'envoi est fini
        serv_to_client.send("database" + "\end")
    #.On ferme la connection avec le clien afin de laisser la place a un futur 
    #.clien qui voudrais se conecter
    serv_to_client.close()
