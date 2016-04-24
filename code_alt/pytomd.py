#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Import des modules

import sys
import os

# Corps du programme

print("--- Exporteur Python (.py) vers Markdown (.md) ---\n")


file_s_b = open(sys.argv[1], "r")
file_s = file_s_b.read()
file_s_l = file_s.split("\n\n")

comm_l = ""
for ligne in (file_s_l[0]).split("\n"):
    if "ref_to_md" in ligne:
        comm_l = ligne
        break
if not comm_l:
    comm_l = "#ref_to_md"


pos = comm_l.index("ref_to_md")
scomm = (comm_l[:pos]).strip()

print("Balise de commentaire identifiée : >>>{}<<<".format(scomm))

file_s_b.close()

# Début traitement

file_s_b = open(sys.argv[1], "r")


# 1. On peut couper des blocs du fichier d'origine à ne pas inclure dans la 
# doc en les plaçant entre les balises "#$"
# On créé donc un fichier temporaire qui contient la même chose que le fichier
# source à l'exception du code entre ces balises qui n'est pas inclu et qui est
# remplacé par ce qui suit la première balise "#$"
# Le fichier est supprimé à la fin du traitement

file_t_b = open(".{}_comm_temp.py".format((sys.argv[1])[:-3]), "w")

bloc_ouvert = False

ligne = file_s_b.readline()

code = ""
out = ""
remp = ""

while ligne:
    # On enlève les .... et \t
    c = 0
    while ligne[c] == " " or ligne[c] == "\t":
        c += 1
    ligne_mod = ligne[c:]
    # On gère les lignes vides
    if ligne_mod == "\n":
        ligne_mod = "~\n~"
    # On teste
    if ligne_mod[0:2] == scomm + "$":
        if bloc_ouvert:
            out += ligne
            out = ""
            file_t_b.write("{}.{}{}\n\n".format(scomm, ((c + 4) / 4) * ">", remp))
            bloc_ouvert = False
            remp = ""
        elif not bloc_ouvert:
            file_t_b.write(code)
            code = ""
            remp = ligne_mod[2:-1]
            out += ligne
            bloc_ouvert = True
    else:
        if bloc_ouvert:
            out += ligne
        elif not bloc_ouvert:
            code += ligne
    ligne = file_s_b.readline()
if bloc_ouvert:
    file_t_b.write("{}.{}{}\n\n".format(scomm, ((c + 4) / 4) * ">", remp))
elif not bloc_ouvert:
    file_t_b.write(code)
file_s_b.close()
file_t_b.close()

###############################################

file_s_b = open(".{}_comm_temp.py".format((sys.argv[1])[:-3]), "r")

file_d_b = open("{}_comm.md".format((sys.argv[1])[:-3]), "w")

ligne = file_s_b.readline()
ligne = file_s_b.readline()
ligne = file_s_b.readline()
ligne = file_s_b.readline()
while ligne == "\n":
    ligne = file_s_b.readline()

comm = ""
code = ""

flag = "comm"

# Pour chaque ligne :
while ligne:
    # On enlève les .... et \t
    c = 0
    while ligne[c] == " " or ligne[c] == "\t":
        c += 1
    ligne_mod = ligne[c:]
    # On gère les lignes vides
    if ligne_mod == "\n":
        ligne_mod = "~\n~"
    # On teste
    if ligne_mod[0:2] == scomm + ".":
        if flag == "comm":
            comm += ligne_mod[2:]
        elif flag == "code":
            if code[-2:] == "\n\n":
                code = code[:-1]
            code = "```python\n{}```\n".format(code)
            file_d_b.write(code)
            code = ""
            comm += ligne_mod[2:]
            flag = "comm"
    elif ligne_mod[0:2] == "~\n":
        if flag == "comm":
            comm += ligne
        elif flag == "code":
            code += ligne
    else:
        if flag == "comm":
            file_d_b.write(comm)
            comm = ""
            code += ligne
            flag = "code"
        elif flag == "code":
            code += ligne
    ligne = file_s_b.readline()

# On écrit le bloc final
if flag == "comm":
    file_d_b.write(comm)
elif flag == "code":
    if code[-2:] == "\n\n":
        code = code[:-1]
    code = "```python\n{}```\n".format(code)
    file_d_b.write(code)

file_d_b.close()
os.system("rm .{}_comm_temp.py".format((sys.argv[1])[:-3]))

# Fin traitement

print("\n--- Terminé ! ---")
