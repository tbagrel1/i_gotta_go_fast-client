# -*- coding:utf-8 -*

################################################################################
#                                                                              #
#                                 FAST WRITING 2                               #
#                                                                              #
################################################################################

# Titre :                     Fast Writing
# Version :                   V2.0.0 / Python 2
# Affichage :                 Interface graphique (Tkinter)
# Auteur :                    Thomas BAGREL
# Adresse :                   tomsb07@gmail.com

# Import des modules

from __future__ import division
from time import *
from random import *
from Tkinter import *
from io import open
from tkFont import *
from threading import *

# Déclarations des variables globales

global TempsChoisi
TempsChoisi = 30.0
global TempsChoisiBrut
TempsChoisiBrut = ""
global TempsRestant
TempsRestant = 0.0
global TempsInter
TempsInter = 0.0
global TempsDepart
TempsDepart = 0.0
global TempsEcoule
TempsEcoule = 0.0
global JetonTemps
JetonTemps = True
global JetonPause
JetonPause = False
global DebutPause
DebutPause = 0.0
global FinPause
FinPause = 0.0
global MotsJustes
MotsJustes = 0
global TempsParMot
TempsParMot = 0.0
global Erreurs
Erreurs = 0
global MotsRates
MotsRates = 0
global EssaisRestants
EssaisRestants = 3
global RatioTempsMots
RatioTempsMots = 0.0
global MotAffiche
MotAffiche = ""
global MotAfficheBrut
MotAfficheBrut = ""
global MotAttendu
MotAttendu = ""
global MotAttenduBrut
MotAttenduBrut = ""
global MotTapeBrut
MotTapeBrut = ""
global MotTape
MotTape = ""
global ChaineValidation
ChaineValidation = []
global TopValidation
TopValidation = False
global JetonValider
JetonValider = False
global JetonQuitter
JetonQuitter = False
global LigneBrut
LigneBrut = ""
global Ligne
Ligne = ""
global PositionBarre
PositionBarre = 0
global JetonMot
JetonMot = 0
global TempsValidation
TempsValidation = True
global TempsLorsValidation
TempsLorsValidation = 0.0
global TempsDebutPause
TempsDebutPause = 0.0
global TempsFinPause
TempsFinPause = 0.0
global TempsInterPause
TempsInterPause = 0.0
global TempsSuivant
TempsSuivant = 0.0
global TempsPrecedent
TempsPrecedent = 0.0

# Création des classes et fonctions

class ThreadTimer(Thread):
	def __init__(self, threadID, name):
		Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def run(self):
		print("Starting "+self.name)
		FonctionTimer()
		print("Exiting "+self.name)

def QuitterBvn(*event):
	SFenetreBienvenue.quit()

def ValiderTemps(*event):
	global TempsChoisi
	global TempsChoisiBrut
	TempsChoisi = TempsChoisiBrut.get()
	try:
		TempsChoisi = float(TempsChoisi)
		if TempsChoisi >= 10 and TempsChoisi <= 3599.9:
			SFenetreTemps.quit()
		else:
			if TempsChoisi < 10:
				TxtBoxError = Label(SFenetreTemps, text="Entrez une valeur\
 supérieure à 10 s !")
				TxtBoxError.grid(row=3, column=0, columnspan=2,\
 sticky=W+E+N+S)
			if TempsChoisi > 3599.9:
				TxtBoxError = Label(SFenetreTemps, text="Entrez une valeur\
 inférieure à 1 h !")
				TxtBoxError.grid(row=3, column=0, columnspan=2,\
	sticky=W+E+N+S)
	except ValueError:
		TxtBoxError = Label(SFenetreTemps, text="Entrez une valeur numérique\
 correcte !")
		TxtBoxError.grid(row=3, column=0, columnspan=2, sticky=W+E+N+S)
		EntryBoxTemps.delete(0, last=(len(TempsChoisi)+1))

def QuitterTemps(*event):
	global TempsChoisi
	TempsChoisi = 30.0
	SFenetreTemps.quit()

def Commencer(*event):
	EntryBoxMot.configure(state=NORMAL)
	EntryBoxMot.focus_set()
	EntryBoxMot.bind("<Return>", ValiderSaisie)
	EntryBoxMot.bind("<Escape>", PauseToggle)
	BtnCommencer.configure(text="  Pause  ", command=Pause)
	Timer = ThreadTimer(2, "Timer")
	Timer.daemon = True
	Timer.start()
	NouveauMot()

def PauseToggle(*event):
	if JetonPause is False:
		Pause()
	elif JetonPause is True:
		Reprendre()

def Pause(*event):
	global JetonPause
	global TempsDebutPause
	global TempsFinPause
	global TempsInterPause
	global TempsValidation
	if TempsValidation is True :
		JetonPause = True
		EntryBoxMot.configure(state=DISABLED)
		BtnCommencer.configure(text="  Rerendre  ", command=Reprendre)
		TempsDebutPause = time()

def Reprendre(*event):
	global JetonPause
	global TempsValidation
	if TempsValidation is True : 
		JetonPause = False
		EntryBoxMot.configure(state=NORMAL)
		BtnCommencer.configure(text="  Pause  ", command=Pause)

def FonctionTimer():
	global TempsDepart
	global JetonQuitter
	global TempsInter
	global TempsRestant
	global TempsChoisi
	global TempsValidation
	global JetonPause
	global TempsInterPause
	global TempsDebutPause
	global TempsFinPause
	TempsDepart = time()
	while JetonQuitter is False :
		TempsInter = time()
		TempsRestant = TempsChoisi - (TempsInter - TempsDepart)
		if JetonPause is True :
			TxtBoxTimer.configure(state=DISABLED)
			while JetonPause is True :
				sleep(0.1)
			try :
				TempsFinPause = time()
				TempsDepart = TempsDepart + (TempsFinPause - TempsDebutPause)
				TxtBoxTimer.configure(state=NORMAL)
			except :
				pass
		if TempsRestant <= 0.0:
			try :
				TxtBoxTimer.configure(text="0 : 0.0")
				TempsValidation = False
				EffacerSaisie()
				EntryBoxMot.configure(state=DISABLED)
				TxtBoxMot.configure(text="  Terminé  !  ")
				Recommencer()
				return
			except :
				pass
		try :
			TxtBoxTimer.configure(text=str(int(TempsRestant//60))+" : "+str\
(round(TempsRestant%60,1)))
			sleep(0.1)
		except :
			pass
	return

def ValiderSaisie(*event):
	global TempsDepart
	global MotTape
	global MotTapeBrut
	global ChaineDeValidation
	global ValidationGenerale
	global MotAttendu
	global MotAffiche
	global MotsJustes
	global Erreurs
	global EssaisRestants
	global MotsRates
	global TempsValidation
	global TempsLorsValidation
	global RatioTempsMots
	global TempsSuivant
	global TempsPrecedent
	MotTape = (MotTapeBrut.get()).strip()
	ChaineDeValidation=[]
	TempsSuivant = time()
	ValidationGenerale = False
	if TempsValidation is True and JetonPause is False and MotTape != "" and\
 (TempsSuivant - TempsPrecedent) >= 0.25 :
		for i in range (1,(len(MotTape)+1)):
			if MotTape[(i-1):i] == MotAttendu[(i-1):i]:
				ChaineDeValidation.append(1)
			else:
				ChaineDeValidation.append(0)
		if sum(ChaineDeValidation) == len(MotAttendu) and len(MotTape)==\
	len(MotAttendu):
			MotsJustes = MotsJustes + 1
			TxtBoxNombreMotsJustes.configure(text=MotsJustes)
			TempsLorsValidation = time()
			RatioTempsMots = (TempsLorsValidation - TempsDepart) / MotsJustes
			TxtBoxNombreTempsParMot.configure(text=str(round(RatioTempsMots,\
 1)))
			NouveauMot()
		else:
			EffacerSaisie()
			Erreurs = Erreurs + 1
			TxtBoxNombreErreurs.configure(text=Erreurs)
			EssaisRestants = EssaisRestants - 1
			TxtBoxMot.configure(text=MotAffiche+"   ("\
	+str(EssaisRestants)+" essais restants)")
			if EssaisRestants == 0:
				MotsRates = MotsRates + 1
				TxtBoxNombreMotsRates.configure(text=MotsRates)
				NouveauMot()
				EssaisRestants = 3
	TempsPrecedent = time()
	
def EffacerSaisie():
	global MotTape
	global MotTapeBrut
	MotTape = MotTapeBrut.get()
	EntryBoxMot.delete(0, last=(len(MotTape)+1))

def NouveauMot():
	global EssaisRestants
	global MotAttendu
	global MotAttenduBrut
	global JetonMot
	global Ligne
	global LigneBrut
	global PositionBarre
	global MotAffiche
	global MotAfficheBrut
	EffacerSaisie()
	EssaisRestants = 3
	JetonMot = randint(0,len(ListeMots)-1)
	LigneBrut = ListeMots[JetonMot]
	Ligne = LigneBrut[:-1]
	PositionBarre = Ligne.find("|")
	if PositionBarre == -1:
		MotAttendu = Ligne.strip()
		MotAffiche = Ligne.strip()
	else:
		MotAfficheBrut = Ligne[:PositionBarre]
		MotAffiche = MotAfficheBrut.strip()
		MotAttenduBrut = Ligne[(PositionBarre+1):]
		MotAttendu = MotAttenduBrut.strip()
	TxtBoxMot.configure(text=MotAffiche+"   ("+str(EssaisRestants)+" essais \
restants)")

def Quitter(*event):
	global JetonQuitter
	JetonQuitter = True
	Master.quit

def Recommencer():
	pass

# Corps du programme

Master = Tk()
Master.title("Fast Writing")
Master.protocol("WM_DELETE_WINDOW", Master.quit)
Police1 = Font(root=Master, size=14, family="Arial")
Police2 = Font(root=Master, size=20, family="Arial")
Master.grab_set()
Master.focus_set()

# Création des fenêtres de début (Bienvenue)

SFenetreBienvenue = Frame(Master)
Master.protocol("WM_DELETE_WINDOW", SFenetreBienvenue.quit)
SFenetreBienvenue.grid(row=0, column=0, sticky=W+E+N+S)
SFenetreBienvenue.focus_set()
TxtBoxBienvenue = Label(SFenetreBienvenue, text="Bienvenue !\n Avec ce \
programme, vous pourrez développer votre vitesse de frappe au clavier,\n mais\
 également vous améliorer dans la matière de votre choix !\nBonne partie.\n\
\nPour plus d'informations, consultez le fichier \"Lisez-Moi\".")
TxtBoxBienvenue.grid(row=0, column=0, sticky=W+E+N+S)
BoutonFermer = Button(SFenetreBienvenue, text="   Ok   ",\
 command=SFenetreBienvenue.quit)
BoutonFermer.grid(row=1, column=0, sticky=W+E+N+S)
SFenetreBienvenue.bind("<Return>", QuitterBvn)
SFenetreBienvenue.bind("<Escape>", QuitterBvn)
SFenetreBienvenue.mainloop()
SFenetreBienvenue.destroy()

# Choix de la liste de mots

# Ouverture de la liste de mots
with open("ListeMots.txt", "r", encoding="iso-8859-1") as ListeMotsBrut:
	ListeMots = ListeMotsBrut.readlines()

# Création des fenêtres de début (Temps)

SFenetreTemps = Frame(Master)
SFenetreTemps.grid(row=0, column=0, sticky=W+E+N+S)
TxtBoxSaisie = Label(SFenetreTemps, text="Combien de temps voulez-vous jouer ?")
TxtBoxSaisie.grid(row=0, column=0, columnspan=2, sticky=W+E+N+S)
TempsChoisiBrut = StringVar()
EntryBoxTemps= Entry(SFenetreTemps, textvariable=TempsChoisiBrut, width=20)
EntryBoxTemps.grid(row=1, column=0, sticky=W+E+N+S)
EntryBoxTemps.focus_set()
TxtBoxSeconde = Label(SFenetreTemps, text="secondes")
TxtBoxSeconde.grid(row=1, column=1, sticky=W+E+N+S)
BoutonOk = Button(SFenetreTemps, text="   Ok   ", command=ValiderTemps)
BoutonOk.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S)
EntryBoxTemps.bind("<Return>", ValiderTemps)
EntryBoxTemps.bind("<Escape>", QuitterTemps)
SFenetreTemps.bind("<Return>", ValiderTemps)
SFenetreTemps.bind("<Escape>", QuitterTemps)
SFenetreTemps.mainloop()
SFenetreTemps.destroy()
# Fermeture (destruction) des fenêtres de début

# Création des 4 sous-fenêtres (Compteur, Saisie, Timer et Etat)
FenetreCompteur = Frame(Master, cursor="circle", relief="raised", borderwidth=1)
FenetreCompteur.grid(row=0, column=0, sticky=N+S)
FenetreSaisie = Frame(Master, cursor="xterm", relief="raised", borderwidth=1)
FenetreSaisie.grid(row=0, column=1)
FenetreTimer = Frame(Master, cursor="watch", relief="raised", borderwidth=1)
FenetreTimer.grid(row=0, column=2, sticky=N+S)
FenetreEtat = Frame(Master, cursor="arrow")
FenetreEtat.grid(row=1, column=0, columnspan=3)

# Remplissage de la fenêtre Timer
TxtBoxTemps = Label(FenetreTimer, text="\n\n\nTemps restant :", font=Police1)
TxtBoxTemps.grid(row=0, column=0, sticky=W+E+N+S, padx=10, pady=15)
TxtBoxTimer = Label(FenetreTimer, text=str(int(TempsChoisi//60))+" : "\
+str(round(TempsChoisi%60,1)), font=Police2, width=15)
TxtBoxTimer.grid(row=1, column=0, sticky=W+E+N+S, padx=10, pady=15)

# Remplissage de la fenêtre Saisie
TxtBoxSaisie = Label(FenetreSaisie, text="Mot à taper :", font=Police1)
TxtBoxSaisie.grid(row=0, column=0, columnspan=2, sticky=W+E+N+S, padx=10,\
 pady=15)
TxtBoxMot = Label(FenetreSaisie, text="", font=Police2, bg="yellow", width=25)
TxtBoxMot.grid(row=1, column=0, columnspan=2, sticky=W+E+N+S, padx=10, pady=15)
MotTapeBrut = StringVar()
EntryBoxMot = Entry(FenetreSaisie, textvariable=MotTapeBrut, font=Police2,\
 width=25)
EntryBoxMot.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S, padx=10,\
 pady=15)
EntryBoxMot.configure(state=DISABLED)
BtnValider = Button(FenetreSaisie, text="Valider", command=ValiderSaisie,\
 width=8)
BtnValider.grid(row=3, column=0, padx=100, pady=15, sticky=W+E+N+S)
BtnEffacer = Button(FenetreSaisie, text="Effacer", command=EffacerSaisie,\
 width=8)
BtnEffacer.grid(row=3, column=1, padx=100, pady=15, sticky=W+E+N+S)

# Remplissage de la fenêtre Compteur
TxtBoxMotsJustes = Label(FenetreCompteur, text="\nMots justes : ", font=Police2)
TxtBoxMotsJustes.grid(row=0, column=0, sticky=W+N+S, padx=5, pady=5)
TxtBoxNombreMotsJustes = Label(FenetreCompteur, text="\n"+str(MotsJustes),\
 font=Police2)
TxtBoxNombreMotsJustes.grid(row=0, column=1, sticky=E+N+S, padx=5, pady=5)
TxtBoxTempsParMot = Label(FenetreCompteur, text="Temps par mot : ",\
 font=Police1)
TxtBoxTempsParMot.grid(row=1, column=0, sticky=W+N+S, padx=5, pady=5)
TxtBoxNombreTempsParMot = Label(FenetreCompteur, text=str(TempsParMot)+" s",\
 font=Police1)
TxtBoxNombreTempsParMot.grid(row=1, column=1, sticky=E+N+S, padx=5, pady=5)
TxtBoxSeparation = Label(FenetreCompteur, text="____________________",\
 font=Police2, width=15)
TxtBoxSeparation.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S,\
 padx=10, pady=5)
TxtBoxErreurs = Label(FenetreCompteur, text="Erreurs : ", font=Police1)
TxtBoxErreurs.grid(row=3, column=0, sticky=W+N+S, padx=5, pady=5)
TxtBoxNombreErreurs = Label(FenetreCompteur, text=str(Erreurs), font=Police1,\
 fg="red")
TxtBoxNombreErreurs.grid(row=3, column=1, sticky=E+N+S, padx=5, pady=5)
TxtBoxMotsRates = Label(FenetreCompteur, text="Mots ratés : ", font=Police1)
TxtBoxMotsRates.grid(row=4, column=0, sticky=W+N+S, padx=5, pady=5)
TxtBoxNombreMotsRates = Label(FenetreCompteur, text=str(MotsRates),\
 font=Police1, fg="red")
TxtBoxNombreMotsRates.grid(row=4, column=1, sticky=E+N+S, padx=5, pady=5)

# Remplissage de la fenêtre Etat
NoteBas = Label(FenetreEtat, text="Fast Writing V2.0.0 Beta - Thomas BAGREL \
- 2015 / 2016")
NoteBas.grid(row=1, column=0, columnspan=2, sticky=W+E+N+S, pady = 10)
BtnCommencer = Button(FenetreEtat, text="Commencer !", command=Commencer,\
 width=8)
BtnCommencer.grid(row=0, column=0, sticky=W+E+N+S, padx=10, pady=5)
BtnQuitter = Button(FenetreEtat, text="Quitter", command=Master.quit,\
 width=8)
BtnQuitter.grid(row=0, column=1, sticky=W+E+N+S, padx=10, pady=5)

# Fin du programme

# Boucle de fin de l'interface graphique (fermeture)
Master.mainloop()
Master.destroy()
