# -*- coding: utf-8 -*

# Import des modules
from Tkinter import *
from time import *

# Déclaration des classes

class TimerApplication(Frame):
    def __init__(self, temps=10.0, ligne=0, colonne=0, mode="-", parent=None):
        Frame.__init__(self, parent)
        self.LabelTempsT = Label(self, text="Time", justify=CENTER)
        self.LabelTempsT.grid(row=0, column=0, sticky=W + E + N + S)
        self.LabelTempsV = Label(self, text="00:00.0 / 00:00.0")
        self.LabelTempsV.grid(row=1, column=0, sticky=W + E + N + S)
        self.BoutonStartPause = Button(self, text="Start",
                                       command=self.startPauseToggle)
        self.BoutonStartPause.grid(row=2, column=0, sticky=W + E + N + S)
        self.grid(row=ligne, column=colonne)
        self.mode = mode
        self.temps_debut = time()
        self.temps_debut_pause = self.temps_debut
        self.temps_fin_pause = 0.0
        self.temps_choisi = temps
        self.temps_ecoule = 0.0
        self.temps_restant = self.temps_choisi
        self.jeton_pause = True
        self.finiV = False

        if self.mode == "+":
            self.LabelTempsV\
                .configure(text="{}:{} / {}:{}"
                           .format(self.temps_ecoule // 60,
                                   round(self.temps_ecoule % 60, 1),
                                   self.temps_choisi // 60,
                                   round(self.temps_choisi % 60, 1)))
        else:
            self.LabelTempsV\
                .configure(text="{}:{} / {}:{}"
                           .format(self.temps_restant // 60,
                                   round(self.temps_restant % 60, 1),
                                   self.temps_choisi // 60,
                                   round(self.temps_choisi % 60, 1)))

        self.majTemps()

    def majTemps(self):
        if not self.jeton_pause:
            self.temps_ecoule = time() - self.temps_debut
            if self.mode == "+":
                self.LabelTempsV\
                    .configure(text="{}:{} / {}:{}"
                               .format(self.temps_ecoule // 60,
                                       round(self.temps_ecoule % 60, 1),
                                       self.temps_choisi // 60,
                                       round(self.temps_choisi % 60, 1)))
                if self.temps_ecoule >= self.temps_choisi:
                    self.temps_ecoule = self.temps_choisi
                    self.LabelTempsV\
                        .configure(text="{}:{} / {}:{}"
                                   .format(self.temps_ecoule // 60,
                                           round(self.temps_ecoule % 60, 1),
                                           self.temps_choisi // 60,
                                           round(self.temps_choisi % 60, 1)))
                    self.fini()
            else:
                self.temps_restant = self.temps_choisi - self.temps_ecoule
                self.LabelTempsV\
                    .configure(text="{}:{} / {}:{}"
                               .format(self.temps_restant // 60,
                                       round(self.temps_restant % 60, 1),
                                       self.temps_choisi // 60,
                                       round(self.temps_choisi % 60, 1)))
                if self.temps_restant <= 0.0:
                    self.temps_restant = 0.0
                    self.LabelTempsV\
                        .configure(text="{}:{} / {}:{}"
                                   .format(self.temps_restant // 60,
                                           round(self.temps_restant % 60, 1),
                                           self.temps_choisi // 60,
                                           round(self.temps_choisi % 60, 1)))
                    self.fini()

        self.after(100, self.majTemps)

    def startPauseToggle(self):
        # Si le jeu est en pause ou n'a pas encore commencé
        if self.finiV:
            self.temps_debut = time()
            self.temps_debut_pause = self.temps_debut
            self.temps_fin_pause = 0.0
            self.temps_ecoule = 0.0
            self.temps_restant = self.temps_choisi
            self.jeton_pause = True
            self.finiV = False
            self.BoutonStartPause.configure(text="Start")
            if self.mode == "+":
                self.LabelTempsV\
                    .configure(text="{}:{} / {}:{}"
                               .format(self.temps_ecoule // 60,
                                       round(self.temps_ecoule % 60, 1),
                                       self.temps_choisi // 60,
                                       round(self.temps_choisi % 60, 1)))
            else:
                self.LabelTempsV\
                    .configure(text="{}:{} / {}:{}"
                               .format(self.temps_restant // 60,
                                       round(self.temps_restant % 60, 1),
                                       self.temps_choisi // 60,
                                       round(self.temps_choisi % 60, 1)))
            return
        else:
            if self.jeton_pause:
                self.BoutonStartPause.configure(text="Pause")
                self.jeton_pause = False
                self.temps_fin_pause = time()
                self.temps_debut += (self.temps_fin_pause - 
                                     self.temps_debut_pause)
            else:
                self.BoutonStartPause.configure(text="Start")
                self.jeton_pause = True
                self.temps_debut_pause = time()

    def fini(self):
        self.finiV = True
        self.BoutonStartPause.configure(text="Restart")

if __name__ == '__main__':
    Master = Tk()                          # On créé une application Tkinter
    fen = TimerApplication(temps=30,       # Temps où le timer s'arrête
                           ligne=0,        # Ligne où le timer est grid
                           colonne=0,      # Colonne où le timer est grid
                           mode="+",       # Mode de fonctionnement : 0->temps
                           parent=Master)  # Fenêtre parente
    Master.mainloop()                      # On lance la boucle d'événements

# N.B. : On peut aussi créér la fenêtre avec les paramètres par défaut :
# fen = TimerApplication()
