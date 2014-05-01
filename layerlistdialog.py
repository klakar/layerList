# -*- coding: utf-8 -*-
"""
/***************************************************************************
 layerListDialog
                                 A QGIS plugin
 Manage common layers in lists, making it easier and quicker to add them to projects.
                             -------------------
        begin                : 2014-05-01
        copyright            : (C) 2014 by Klas Karlsson
        email                : klaskarlsson@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_layerlist_create import Ui_layerListCreator
from ui_layerlist_add import Ui_layerListAdd
# create the dialog for zoom to point


class layerListDialogAdd(QtGui.QDialog, Ui_layerListAdd):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

class layerListDialogCreate(QtGui.QDialog, Ui_layerListCreator):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
