#!/usr/bin/python2
# -*- coding: utf-8 -*

import os

print("Début (30 s restant)\n...")
os.system("pandoc -r markdown ../_sources_doc/main_comm.md -t latex -o ../doc/main_comm.pdf")
print("Fini !")
