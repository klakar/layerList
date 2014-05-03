# -*- coding: utf-8 -*-
"""
/***************************************************************************
 layerList
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Manage canvas in "iface"
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from layerlistdialog import *
import os.path
# Adaptation for UTF-8
import codecs

#global layers
#layers = ""

# Global lists
layerProvider = []
layerName = []
layerSource = []






class layerList:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'layerlist_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialogs (after translation) and keep reference
        self.dlgCreate = layerListDialogCreate()
	self.dlgAdd = layerListDialogAdd()
    

    def initGui(self):
        # Create action that will start plugin configuration for the layer list creation
        self.listCreate = QAction(
            QIcon(":/plugins/layerlist/icon1.png"),
            QApplication.translate("LayerList",u"Layer List Creator"), self.iface.mainWindow())
        # connect the action to the run method Create layer list
        self.listCreate.triggered.connect(self.runCreate)
        # Create action that will start plugin configuration for the add from layer list
        self.listAdd = QAction(
            QIcon(":/plugins/layerlist/icon2.png"),
            QApplication.translate("LayerList",u"Add from Layer List"), self.iface.mainWindow())
        # connect the action to the run method Add from layer list
        self.listAdd.triggered.connect(self.runAdd)

        # Add toolbar buttons and menu items
        self.iface.addToolBarIcon(self.listCreate)
        self.iface.addPluginToMenu(QApplication.translate("LayerList",u"&Layer List"), self.listCreate)
        self.iface.addToolBarIcon(self.listAdd)
        self.iface.addPluginToMenu(QApplication.translate("LayerList",u"&Layer List"), self.listAdd)

	# Create action for the add layer list button in the layerlistadd dialog
	self.dlgAdd.btnFindList.clicked.connect(self.findList)

	# Create action for the show help button in the two dialogs
	self.dlgAdd.btnHelp.clicked.connect(self.showHelp)
	self.dlgCreate.btnHelp.clicked.connect(self.showHelp)


    # Show Help files
    def showHelp(self):
	showPluginHelp(filename="help/index")


    # Copy active layers from QGIS to a list widget and create a string variable ready to save...
    def loadActiveLayers(self): 
	self.dlgCreate.listWidget.clear() # Clear the list widget before it is filled again
	canvas = iface.mapCanvas()
	activeLayers = canvas.layers() # Create list with all active layers
	layers = u"# Layer List - QGIS Plugin by Klas Karlsson\n" # Create list header and "test" line in a text string
	for layer in reversed(activeLayers): # Repeat for all layers in the list
	    layerType = layer.type() # Is it Vector or Raster?
	    layerSource = layer.publicSource() # path or command for the layer source
	    provider = layer.providerType() # Example org, gdal, wms, wfs, postgres, etc
	    if layerType == QgsMapLayer.VectorLayer:
		layers = layers + (u"%s,%s,%s\n" % (provider, layer.name(), layerSource))
		self.dlgCreate.listWidget.addItem(layer.name()) # Add the layer name to the list
	    if layerType == QgsMapLayer.RasterLayer:
		layers = layers + (u"%s,%s,%s\n" % (provider, layer.name(), layerSource))
		self.dlgCreate.listWidget.addItem(layer.name()) # Add the layer name to the list
	return layers	# Send back all the layers in a text string ready to be saved to a file





    # Add from layer list dialog button ... to select a layer list file to load into the list widget. File extension *.qll is used for these files but any filename is fine.
    def findList(self):
	fileName = QFileDialog.getOpenFileName(None, QApplication.translate("LayerList",u"Open File"), None, QApplication.translate("LayerList",u"QGIS Layer Lists (*.qll);; All files (*.*)"))
	if fileName != "": # If no file is selected, do nothing.
		self.dlgAdd.lblListFile.setText(fileName) # Write the file path to a label in the dialog
		s = QSettings()
		s.setValue("loadlayers/listfile", fileName) # Also save the path to a QGIS variable in order to remember it for next time
		self.updateList() # While we're at it, populate the list widget with the layers from the selected list





    # Uppdate the list widget from the Add from layer list dialog with layers from the current list file
    def updateList(self):
	# First clear the list widget
	self.dlgAdd.listWidget.clear()
	# Get the current list file path
	s = QSettings()
	fileName = s.value("loadlayers/listfile", QApplication.translate("LayerList",u"Layer List Missing")) # If no file is current, a "List Missing" text is passed.
	self.dlgAdd.lblListFile.setText(fileName) # Update the text in the dialog

	# Read from the layer list file, if it exist
	if fileName != QApplication.translate("LayerList",u"Layer List Missing"):
	   try: # Test the file by openin it and reading the first row.
	   	ff = codecs.open(fileName, 'r', 'utf-8')
	   	firstRow = ff.readline().strip()
	   	ff.close()
		# The first row is a test to see if it is a valid layer list file
	   	if firstRow != "# Layer List - QGIS Plugin by Klas Karlsson": # This test text is created in the LoadActiveLayers function
			QMessageBox.information(self.iface.mainWindow(),QApplication.translate("LayerList",u"Error"), QApplication.translate("LayerList",u"Layer List file is damaged \n First row in the file must be:\n# Layer List - QGIS Plugin by Klas Karlsson\n\nLayer rows are written with the syntax:\nLayerProvider,LayerName,LayerPath\n\Reload the plug-in or restart QGIS."))
			s = QSettings()
			s.remove("loadlayers/listfile") # Remove the reference to the faulty current file
	   except: # If the file can't be read, and understood (i.e. not a text file)...	
		s = QSettings()
		s.remove("loadlayers/listfile") # Remove the reference to the faulty current file
		self.dlgAdd.lblListFile.setText(QApplication.translate("LayerList",u"Layer List Missing"))
		QMessageBox.information(self.iface.mainWindow(),QApplication.translate("LayerList",u"Error"), QApplication.translate("LayerList",u"This file could not be read.\nTry another file.\n\nYou must reload the plug-in or restart QGIS first."))

	   # Well if nothing went south, it's time to load the list into the list widget.
	   f = codecs.open(fileName, 'r', 'utf-8')
	   for line in f: # Repeat for every line in the list file
		fileData = line.strip() # Remove any new line characters from the line (strip)
		if fileData != "": # Ignore empty lines
		    if fileData[:1] != "#": # Ignore lines that start with hasch-tag
			tempList = fileData.split(",") # Separate the line by comma signs and put it in a temporary list
			layerProvider.append( tempList[0] ) # Add the first item to the layerProvider list
			layerName.append( tempList[1] ) # Add the second item to the layerName list
			layerSource.append( tempList[2] ) # Add the third item to the layerSource list
			self.dlgAdd.listWidget.addItem(tempList[1]) # Add the Name of the layer to the list widget.
	   f.close() # Close the file... Doh!






    def unload(self):
        # Remove the plugin menu items and icons
        self.iface.removePluginMenu(QApplication.translate("LayerList",u"&Layer List"), self.listCreate)
        self.iface.removeToolBarIcon(self.listCreate)
        self.iface.removePluginMenu(QApplication.translate("LayerList",u"&Layer List"), self.listAdd)
        self.iface.removeToolBarIcon(self.listAdd)




    # run method for the layer list creation part
    def runCreate(self):
        # show the dialog
	layers = self.loadActiveLayers()
        self.dlgCreate.show()
        # Run the dialog event loop
        result = self.dlgCreate.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            fileName = QFileDialog.getSaveFileName(None, QApplication.translate("LayerList",u"Save File"), ".qll")
	    if fileName != "":
		saveFile = codecs.open(fileName, 'w', 'utf-8')
		saveFile.write(layers)
		saveFile.close()
		# Ask if the new file should be used as new current layer list
		reply = QMessageBox.question(self.iface.mainWindow(),QApplication.translate("LayerList",u"New List file"), QApplication.translate("LayerList",u"Do you want to use this file as new current List File?"), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			s = QSettings()
			s.setValue("loadlayers/listfile", fileName) # Save path to QGIS variable in order to remember it for next time



    # run method for the add from layer list part
    def runAdd(self):
	# update the list
	self.updateList()
        # show the dialog
        self.dlgAdd.show()
        # Run the dialog event loop
        result = self.dlgAdd.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            mark = self.dlgAdd.listWidget.selectedItems()
	    for i in list(mark):
		index = layerName.index(i.text()) # Vilket index har valt lager
		if layerProvider[index].upper() in "OGR WFS POSTGRES GPX SPATIALITE MSSQL SQLANYWHERE DELIMITEDTEXT GRASS":
			layer = QgsVectorLayer(layerSource[index], layerName[index], layerProvider[index])
		if layerProvider[index].upper() in "WMS RASTER GDAL WCS":
			layer = QgsRasterLayer(layerSource[index], layerName[index], layerProvider[index])
		if not layer.isValid():
			QMessageBox.information(self.iface.mainWindow(),QApplication.translate("LayerList",u"Error!"), QApplication.translate("LayerList",u"%s is not a valid layer:\n %s") % (layerName[index], layerSource[index]))
			break
		QgsMapLayerRegistry.instance().addMapLayer(layer)


