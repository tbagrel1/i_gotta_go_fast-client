#!/usr/bin/python3
# -*- coding: utf-8 -*-

# On importe "sys" pour utiliser "argv"
import sys
# On importe les fichiers de base de PyQt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# On importe notre fenêtre définie dans le .ui et le .py associé
# La syntaxe est :
# "from <nom> import Ui_<nom>"
# avec <nom> le nom du fichier .ui et .py associé sans l'extension 
from sfenetre1 import Ui_sfenetre1

# On peut remplacer "TestApplication" par le nom de notre classe-app
# "QDialog" est la classe parente désignée dans QtDesigner
class TestApplication(QDialog):

	# Les deux premières lignes sont obligatoires
	def __init__(self, parent=None):
		# On remplacera "TestApplication" par le nom choisi plus haut
		super(TestApplication, self).__init__(parent)
		# On appelle la fonction "createWidgets()"
		self.createWidgets()

	# On définit la fonction "createWidgets"
	def createWidgets(self):
		# L'attribut self.ui est une instance de notre GUI définie dans le .ui et .py associé
		self.ui = Ui_sfenetre1()
		# On setup le GUI
		self.ui.setupUi(self)

# Si le programme est exécuté directement
if __name__ == "__main__":
	# "app" est une application Qt ("QApplication" est la classe générale)
	# On passe en paramètres les arguments passés au script
	app = QApplication(sys.argv)
	# On instancie un objet de la classe créée plus haut
	myapp = TestApplication()
	# On affiche cette objet
	myapp.show()
	# On connecte la fin du script à la fin du GUI
	sys.exit(app.exec_())
