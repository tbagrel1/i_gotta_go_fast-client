# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sfenetre1.ui'
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

class Ui_sfenetre1(object):
    def setupUi(self, sfenetre1):
        sfenetre1.setObjectName(_fromUtf8("sfenetre1"))
        sfenetre1.resize(400, 300)
        self.pushButton = QtGui.QPushButton(sfenetre1)
        self.pushButton.setGeometry(QtCore.QRect(20, 250, 80, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(sfenetre1)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 250, 80, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.spinBox = QtGui.QSpinBox(sfenetre1)
        self.spinBox.setGeometry(QtCore.QRect(130, 110, 47, 24))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.lcdNumber = QtGui.QLCDNumber(sfenetre1)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 150, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

        self.retranslateUi(sfenetre1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.spinBox.stepUp)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.spinBox.stepDown)
        QtCore.QMetaObject.connectSlotsByName(sfenetre1)

    def retranslateUi(self, sfenetre1):
        sfenetre1.setWindowTitle(_translate("sfenetre1", "Dialog", None))
        self.pushButton.setText(_translate("sfenetre1", "+1", None))
        self.pushButton_2.setText(_translate("sfenetre1", "-1", None))

