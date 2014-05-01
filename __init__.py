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
 This script initializes the plugin, making it known to QGIS.
"""
# Buttons in layer toolbar
def category():
  return "Layers"


def classFactory(iface):
    # load layerList class from file layerList
    from layerlist import layerList
    return layerList(iface)
