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
        self.buttonBox = QtGui.QDialogButtonBox(sfenetre1)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(sfenetre1)
        self.label.setGeometry(QtCore.QRect(130, 90, 59, 15))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(sfenetre1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), sfenetre1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), sfenetre1.reject)
        QtCore.QMetaObject.connectSlotsByName(sfenetre1)

    def retranslateUi(self, sfenetre1):
        sfenetre1.setWindowTitle(_translate("sfenetre1", "Dialog", None))
        self.label.setText(_translate("sfenetre1", "Test", None))

