#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import des modules

import sys

# Corps du programme

print("--- Exporteur Python (.py) vers Markdown (.md) ---\n")

# Début traitement

file_s_b = open(sys.argv[1], "r")

file_d_b = open("{}_comm.md".format((sys.argv[1])[:-3]), "w")

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
    if ligne_mod[0:2] == "#.":
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

# Fin traitement

print("\n--- Terminé ! ---")
