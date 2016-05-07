# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/FenetreBVN/fenetrebvn.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FenetreBVN(object):
    def setupUi(self, FenetreBVN):
        FenetreBVN.setObjectName(_fromUtf8("FenetreBVN"))
        FenetreBVN.resize(600, 370)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FenetreBVN.sizePolicy().hasHeightForWidth())
        FenetreBVN.setSizePolicy(sizePolicy)
        FenetreBVN.setMinimumSize(QtCore.QSize(600, 370))
        FenetreBVN.setMaximumSize(QtCore.QSize(600, 370))
        self.FondIcone = QtGui.QGraphicsView(FenetreBVN)
        self.FondIcone.setGeometry(QtCore.QRect(20, 20, 561, 151))
        self.FondIcone.setObjectName(_fromUtf8("FondIcone"))
        self.LabelDescription = QtGui.QLabel(FenetreBVN)
        self.LabelDescription.setGeometry(QtCore.QRect(20, 180, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LabelDescription.setFont(font)
        self.LabelDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelDescription.setWordWrap(True)
        self.LabelDescription.setObjectName(_fromUtf8("LabelDescription"))
        self.LabelCredits = QtGui.QLabel(FenetreBVN)
        self.LabelCredits.setGeometry(QtCore.QRect(20, 309, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LabelCredits.setFont(font)
        self.LabelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelCredits.setObjectName(_fromUtf8("LabelCredits"))
        self.BoutonQuitter = QtGui.QPushButton(FenetreBVN)
        self.BoutonQuitter.setGeometry(QtCore.QRect(20, 250, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BoutonQuitter.setFont(font)
        self.BoutonQuitter.setObjectName(_fromUtf8("BoutonQuitter"))
        self.BoutonContinuer = QtGui.QPushButton(FenetreBVN)
        self.BoutonContinuer.setGeometry(QtCore.QRect(310, 250, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BoutonContinuer.setFont(font)
        self.BoutonContinuer.setObjectName(_fromUtf8("BoutonContinuer"))
        self.LabelIcone = QtGui.QLabel(FenetreBVN)
        self.LabelIcone.setGeometry(QtCore.QRect(20, 20, 561, 151))
        self.LabelIcone.setText(_fromUtf8(""))
        self.LabelIcone.setObjectName(_fromUtf8("LabelIcone"))

        self.retranslateUi(FenetreBVN)
        QtCore.QMetaObject.connectSlotsByName(FenetreBVN)

    def retranslateUi(self, FenetreBVN):
        FenetreBVN.setWindowTitle(_translate("FenetreBVN", "FenetreBVN", None))
        self.LabelDescription.setText(_translate("FenetreBVN", "Ce petit logiciel a pour but de vous aider à taper plus vite au clavier, en particulier les mots les plus utilisés de la langue Française", None))
        self.LabelCredits.setText(_translate("FenetreBVN", "- Thomas BAGREL, Julien ROMARY - Version V1.0.0 - 04/03/2016 -\n"
"tomsb07@gmail.com", None))
        self.BoutonQuitter.setText(_translate("FenetreBVN", "Quitter", None))
        self.BoutonContinuer.setText(_translate("FenetreBVN", "Continuer", None))

