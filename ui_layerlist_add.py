# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_layerlist_add.ui'
#
# Created: Thu May  1 15:45:21 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_layerListAdd(object):
    def setupUi(self, layerListAdd):
        layerListAdd.setObjectName(_fromUtf8("layerListAdd"))
        layerListAdd.resize(391, 320)
        self.buttonBox = QtGui.QDialogButtonBox(layerListAdd)
        self.buttonBox.setGeometry(QtCore.QRect(10, 280, 371, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lblReadList = QtGui.QLabel(layerListAdd)
        self.lblReadList.setGeometry(QtCore.QRect(10, 10, 371, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblReadList.setFont(font)
        self.lblReadList.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.lblReadList.setObjectName(_fromUtf8("lblReadList"))
        self.listWidget = QtGui.QListWidget(layerListAdd)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 371, 201))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.lblListFile = QtGui.QLabel(layerListAdd)
        self.lblListFile.setGeometry(QtCore.QRect(10, 250, 341, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblListFile.setFont(font)
        self.lblListFile.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.lblListFile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblListFile.setObjectName(_fromUtf8("lblListFile"))
        self.btnFindList = QtGui.QPushButton(layerListAdd)
        self.btnFindList.setGeometry(QtCore.QRect(360, 247, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnFindList.setFont(font)
        self.btnFindList.setObjectName(_fromUtf8("btnFindList"))

        self.retranslateUi(layerListAdd)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), layerListAdd.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), layerListAdd.reject)
        QtCore.QMetaObject.connectSlotsByName(layerListAdd)

    def retranslateUi(self, layerListAdd):
        layerListAdd.setWindowTitle(_translate("layerListAdd", "Add layers from list", None))
        self.lblReadList.setText(_translate("layerListAdd", "Select layers from list...", None))
        self.lblListFile.setText(_translate("layerListAdd", "No Layer List", None))
        self.btnFindList.setText(_translate("layerListAdd", "...", None))

