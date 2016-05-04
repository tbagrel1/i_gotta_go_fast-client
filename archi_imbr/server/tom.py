#!/usr/bin/python2
# -*- coding: utf-8 -*

from __future__ import division
from random import randint

tot_tombes = 0
tot_traverses = 0

n = input("Nombre de répétitions :\n>>>")

i = 0
per_prec = 0

print("\nAvancement :")
while i < n:
	tomber = False
	x = 0
	y = 0
	while not tomber and x < 10:
		x += 1
		y += randint(-1, 1)
		if y > 1 or y < -1:
			tomber = True
	if tomber:
		tot_tombes += 1
	else:
		tot_traverses += 1
	per = int(round((i / n) * 100, 0))
	if per != per_prec:
		print("{} %".format(per))
		per_prec = per
	i += 1

print("p(\"Tom est tombé\") = {}".format(round(tot_tombes / (tot_tombes + tot_traverses), 6)))
print("p(\"Tom a traversé\") = {}".format(round(tot_traverses / (tot_traverses + tot_tombes), 6)))
