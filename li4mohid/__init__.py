# -*- coding: utf-8 -*-
"""
/***************************************************************************
 test
                                 A QGIS plugin
 Runs model on background
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-10-21
        copyright            : (C) 2019 by Xunta de Galicia
        email                : pmontero@intecmar.es
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load test class from file test.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .li4mohid import li4mohid
    return li4mohid(iface)
