#!/usr/bin/python2
# -*- coding: utf-8 -*

# Import des modules

import hashlib
import sys

def envoyer_score(score):
	code = "test1234"
	checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
	fichier_score = open("fichier_score.txt", "a")
	fichier_score.write("({}, {}, {})\n".format(code, checksum, score))
	fichier_score.close()
