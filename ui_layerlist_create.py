# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_layerlist_create.ui'
#
# Created: Fri May  2 19:38:28 2014
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

class Ui_layerListCreator(object):
    def setupUi(self, layerListCreator):
        layerListCreator.setObjectName(_fromUtf8("layerListCreator"))
        layerListCreator.resize(400, 282)
        self.buttonBox = QtGui.QDialogButtonBox(layerListCreator)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 351, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lblCreateList = QtGui.QLabel(layerListCreator)
        self.lblCreateList.setGeometry(QtCore.QRect(10, 10, 371, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblCreateList.setFont(font)
        self.lblCreateList.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.lblCreateList.setObjectName(_fromUtf8("lblCreateList"))
        self.listWidget = QtGui.QListWidget(layerListCreator)
        self.listWidget.setGeometry(QtCore.QRect(15, 31, 371, 201))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.btnHelp = QtGui.QPushButton(layerListCreator)
        self.btnHelp.setGeometry(QtCore.QRect(10, 250, 21, 21))
        self.btnHelp.setObjectName(_fromUtf8("btnHelp"))

        self.retranslateUi(layerListCreator)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), layerListCreator.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), layerListCreator.reject)
        QtCore.QMetaObject.connectSlotsByName(layerListCreator)

    def retranslateUi(self, layerListCreator):
        layerListCreator.setWindowTitle(_translate("layerListCreator", "Layer List Creator", None))
        self.lblCreateList.setText(_translate("layerListCreator", "Saving layers to list...", None))
        self.btnHelp.setToolTip(_translate("layerListCreator", "Show Plug-In help files (HTML).", None))
        self.btnHelp.setText(_translate("layerListCreator", "?", None))

