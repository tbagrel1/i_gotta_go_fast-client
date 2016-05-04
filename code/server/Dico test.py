# -*- coding:utf-8 -*
DicoScore1 = {}
DicoScore2 = {}
DicoScore3 = {}
DicoScore4 = {}

DicoScore1 = {"pseudo": "test1", "score": 1000, "cpm": 120,
 "cpm": 40, "temps": 120, "d_h": ("27/04/2016","13:15"),
 "texte_t": "Léo le cerf co", "texte_mode": "expl::1"}
 
DicoScore2 = {"pseudo": "test1", "score": 1000, "cpm": 120,
 "cpm": 40, "temps": 120, "d_h": ("27/04/2016","13:15"),
 "texte_t": "Léo le cerf co", "texte_mode": "expl::1"}
 
DicoScore3 = {"pseudo": "test1", "score": 1000, "cpm": 120,
 "cpm": 40, "temps": 120, "d_h": ("27/04/2016","13:15"),
 "texte_t": "Léo le cerf co", "texte_mode": "expl::1"}
 
DicoScore4 = {"pseudo": "test1", "score": 1000, "cpm": 120,
 "cpm": 40, "temps": 120, "d_h": ("27/04/2016","13:15"),
 "texte_t": "Léo le cerf co", "texte_mode": "expl::1"}
 
checksum = DicoScore1["temps"] * DicoScore1["score"]

for key in DicoScore1:
	DicoScore1[key] = DicoScore1[key].crypt("clé secrète")
checksum = checksum.crypt("clé secrète")
MetaDico1 = (checksum, DicoScore1)
fichier_texte = open()
pickler
pickle(MetaDico1) dans fichier_texte
close
fichier open()
read()
->

Serveur
écrire la string dans un fichier
open fichier
unpickle
try decrypt checksum et tous les elt de DicoScore1
erreur -> score faux
vérifie checksum == calcul checksum Dico




prendre le dico score
pickle dans fichier_texte
open() + read()
cript la chene
=> serve

Scores = [DicoScore1 ,DicoScore2 ,DicoScore3 ,DicoScore4]

for DicoScore in Scores:
	print DicoScore["pseudo"]
