# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/Module/module.ui'
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

class Ui_Module(object):
    def setupUi(self, Module):
        Module.setObjectName(_fromUtf8("Module"))
        Module.resize(1200, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Module.sizePolicy().hasHeightForWidth())
        Module.setSizePolicy(sizePolicy)
        Module.setMinimumSize(QtCore.QSize(1200, 600))
        Module.setMaximumSize(QtCore.QSize(1200, 600))
        self.Frame = QtGui.QWidget(Module)
        self.Frame.setObjectName(_fromUtf8("Frame"))
        self.SFrameAvancement = QtGui.QFrame(self.Frame)
        self.SFrameAvancement.setGeometry(QtCore.QRect(20, 150, 281, 411))
        self.SFrameAvancement.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SFrameAvancement.setFrameShadow(QtGui.QFrame.Raised)
        self.SFrameAvancement.setObjectName(_fromUtf8("SFrameAvancement"))
        self.LabelAvancement = QtGui.QLabel(self.SFrameAvancement)
        self.LabelAvancement.setGeometry(QtCore.QRect(20, 20, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelAvancement.setFont(font)
        self.LabelAvancement.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelAvancement.setObjectName(_fromUtf8("LabelAvancement"))
        self.BarreAvancement = QtGui.QProgressBar(self.SFrameAvancement)
        self.BarreAvancement.setGeometry(QtCore.QRect(60, 50, 161, 341))
        self.BarreAvancement.setProperty("value", 56)
        self.BarreAvancement.setTextVisible(False)
        self.BarreAvancement.setOrientation(QtCore.Qt.Vertical)
        self.BarreAvancement.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.BarreAvancement.setObjectName(_fromUtf8("BarreAvancement"))
        self.SFrameTemps = QtGui.QFrame(self.Frame)
        self.SFrameTemps.setGeometry(QtCore.QRect(900, 150, 281, 411))
        self.SFrameTemps.setAutoFillBackground(False)
        self.SFrameTemps.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SFrameTemps.setFrameShadow(QtGui.QFrame.Raised)
        self.SFrameTemps.setObjectName(_fromUtf8("SFrameTemps"))
        self.LabelStat = QtGui.QLabel(self.SFrameTemps)
        self.LabelStat.setGeometry(QtCore.QRect(20, 140, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelStat.setFont(font)
        self.LabelStat.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelStat.setObjectName(_fromUtf8("LabelStat"))
        self.LabelRestant = QtGui.QLabel(self.SFrameTemps)
        self.LabelRestant.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelRestant.setFont(font)
        self.LabelRestant.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelRestant.setObjectName(_fromUtf8("LabelRestant"))
        self.LabelRestantV = QtGui.QLabel(self.SFrameTemps)
        self.LabelRestantV.setGeometry(QtCore.QRect(10, 50, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.LabelRestantV.setFont(font)
        self.LabelRestantV.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LabelRestantV.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelRestantV.setObjectName(_fromUtf8("LabelRestantV"))
        self.BarreReussite = QtGui.QProgressBar(self.SFrameTemps)
        self.BarreReussite.setGeometry(QtCore.QRect(10, 170, 181, 21))
        self.BarreReussite.setAutoFillBackground(True)
        self.BarreReussite.setProperty("value", 75)
        self.BarreReussite.setTextVisible(False)
        self.BarreReussite.setInvertedAppearance(False)
        self.BarreReussite.setObjectName(_fromUtf8("BarreReussite"))
        self.BarreErreurs = QtGui.QProgressBar(self.SFrameTemps)
        self.BarreErreurs.setGeometry(QtCore.QRect(10, 200, 181, 21))
        self.BarreErreurs.setAutoFillBackground(True)
        self.BarreErreurs.setProperty("value", 25)
        self.BarreErreurs.setTextVisible(False)
        self.BarreErreurs.setInvertedAppearance(True)
        self.BarreErreurs.setObjectName(_fromUtf8("BarreErreurs"))
        self.LabelReussite = QtGui.QLabel(self.SFrameTemps)
        self.LabelReussite.setGeometry(QtCore.QRect(200, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelReussite.setFont(font)
        self.LabelReussite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelReussite.setObjectName(_fromUtf8("LabelReussite"))
        self.LabelErreurs = QtGui.QLabel(self.SFrameTemps)
        self.LabelErreurs.setGeometry(QtCore.QRect(200, 200, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelErreurs.setFont(font)
        self.LabelErreurs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelErreurs.setObjectName(_fromUtf8("LabelErreurs"))
        self.LabelSMots = QtGui.QLabel(self.SFrameTemps)
        self.LabelSMots.setGeometry(QtCore.QRect(200, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelSMots.setFont(font)
        self.LabelSMots.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelSMots.setObjectName(_fromUtf8("LabelSMots"))
        self.Sep1 = QtGui.QFrame(self.SFrameTemps)
        self.Sep1.setGeometry(QtCore.QRect(10, 230, 261, 16))
        self.Sep1.setFrameShape(QtGui.QFrame.HLine)
        self.Sep1.setFrameShadow(QtGui.QFrame.Sunken)
        self.Sep1.setObjectName(_fromUtf8("Sep1"))
        self.LabelSMotsV = QtGui.QLabel(self.SFrameTemps)
        self.LabelSMotsV.setGeometry(QtCore.QRect(20, 250, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LabelSMotsV.setFont(font)
        self.LabelSMotsV.setObjectName(_fromUtf8("LabelSMotsV"))
        self.LabelScore = QtGui.QLabel(self.SFrameTemps)
        self.LabelScore.setGeometry(QtCore.QRect(200, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelScore.setFont(font)
        self.LabelScore.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelScore.setObjectName(_fromUtf8("LabelScore"))
        self.LabelScoreV = QtGui.QLabel(self.SFrameTemps)
        self.LabelScoreV.setGeometry(QtCore.QRect(20, 280, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LabelScoreV.setFont(font)
        self.LabelScoreV.setObjectName(_fromUtf8("LabelScoreV"))
        self.Sep2 = QtGui.QFrame(self.SFrameTemps)
        self.Sep2.setGeometry(QtCore.QRect(10, 310, 261, 20))
        self.Sep2.setFrameShape(QtGui.QFrame.HLine)
        self.Sep2.setFrameShadow(QtGui.QFrame.Sunken)
        self.Sep2.setObjectName(_fromUtf8("Sep2"))
        self.ScoresBox = QtGui.QScrollArea(self.SFrameTemps)
        self.ScoresBox.setGeometry(QtCore.QRect(10, 330, 261, 71))
        self.ScoresBox.setWidgetResizable(True)
        self.ScoresBox.setObjectName(_fromUtf8("ScoresBox"))
        self.SScoresBox = QtGui.QWidget()
        self.SScoresBox.setGeometry(QtCore.QRect(0, 0, 259, 69))
        self.SScoresBox.setObjectName(_fromUtf8("SScoresBox"))
        self.ScoresBox.setWidget(self.SScoresBox)
        self.SFrameTaper = QtGui.QFrame(self.Frame)
        self.SFrameTaper.setGeometry(QtCore.QRect(320, 150, 561, 271))
        self.SFrameTaper.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SFrameTaper.setFrameShadow(QtGui.QFrame.Raised)
        self.SFrameTaper.setObjectName(_fromUtf8("SFrameTaper"))
        self.TextBoxTaper = QtGui.QTextEdit(self.SFrameTaper)
        self.TextBoxTaper.setGeometry(QtCore.QRect(20, 20, 521, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TextBoxTaper.setFont(font)
        self.TextBoxTaper.setObjectName(_fromUtf8("TextBoxTaper"))
        self.EntryTaper = QtGui.QLineEdit(self.SFrameTaper)
        self.EntryTaper.setGeometry(QtCore.QRect(80, 200, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.EntryTaper.setFont(font)
        self.EntryTaper.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryTaper.setObjectName(_fromUtf8("EntryTaper"))
        self.LabelLogo = QtGui.QGraphicsView(self.Frame)
        self.LabelLogo.setGeometry(QtCore.QRect(20, 20, 1161, 111))
        self.LabelLogo.setObjectName(_fromUtf8("LabelLogo"))
        self.SFrameControle = QtGui.QFrame(self.Frame)
        self.SFrameControle.setGeometry(QtCore.QRect(320, 440, 561, 121))
        self.SFrameControle.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SFrameControle.setFrameShadow(QtGui.QFrame.Raised)
        self.SFrameControle.setObjectName(_fromUtf8("SFrameControle"))
        self.BoutonStartPause = QtGui.QPushButton(self.SFrameControle)
        self.BoutonStartPause.setGeometry(QtCore.QRect(10, 60, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BoutonStartPause.setFont(font)
        self.BoutonStartPause.setObjectName(_fromUtf8("BoutonStartPause"))
        self.BoutonQuitter = QtGui.QPushButton(self.SFrameControle)
        self.BoutonQuitter.setGeometry(QtCore.QRect(290, 60, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BoutonQuitter.setFont(font)
        self.BoutonQuitter.setObjectName(_fromUtf8("BoutonQuitter"))
        self.LabelInfo = QtGui.QLabel(self.SFrameControle)
        self.LabelInfo.setGeometry(QtCore.QRect(10, 10, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelInfo.setFont(font)
        self.LabelInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LabelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelInfo.setObjectName(_fromUtf8("LabelInfo"))
        Module.setCentralWidget(self.Frame)
        self.Menu = QtGui.QMenuBar(Module)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 1200, 20))
        self.Menu.setObjectName(_fromUtf8("Menu"))
        Module.setMenuBar(self.Menu)

        self.retranslateUi(Module)
        QtCore.QObject.connect(self.BoutonQuitter, QtCore.SIGNAL(_fromUtf8("clicked()")), Module.close)
        QtCore.QMetaObject.connectSlotsByName(Module)

    def retranslateUi(self, Module):
        Module.setWindowTitle(_translate("Module", "Module", None))
        self.LabelAvancement.setText(_translate("Module", "Avancement", None))
        self.LabelStat.setText(_translate("Module", "Statistiques", None))
        self.LabelRestant.setText(_translate("Module", "Temps / Mots restants", None))
        self.LabelRestantV.setText(_translate("Module", "25 / 30", None))
        self.LabelReussite.setText(_translate("Module", "Réussite", None))
        self.LabelErreurs.setText(_translate("Module", "Erreurs", None))
        self.LabelSMots.setText(_translate("Module", "S / Mots", None))
        self.LabelSMotsV.setText(_translate("Module", "2,01", None))
        self.LabelScore.setText(_translate("Module", "Score", None))
        self.LabelScoreV.setText(_translate("Module", "TextLabel", None))
        self.TextBoxTaper.setHtml(_translate("Module", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte général à <span style=\" color:#ff0000;\">taper</span> &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte général à taper &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte général à taper &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte général à taper &gt;</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt; Texte général à taper &gt;</p></body></html>", None))
        self.EntryTaper.setText(_translate("Module", "tap|er", None))
        self.BoutonStartPause.setText(_translate("Module", "Start / Pause", None))
        self.BoutonQuitter.setText(_translate("Module", "Quitter", None))
        self.LabelInfo.setText(_translate("Module", "Ici des informations sur le programme", None))

