"""
/***************************************************************************
 QGBIF
                                 A QGIS plugin
 qgbif plugin
                               -------------------
        begin                : 2021-04-13
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Alexandre Pierson
        email                : alexandre.pierson40@gmail.com
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


# noinspection PyDocstring,PyPep8Naming
def classFactory(iface):
    """Load QGBIF class from file qgbif.py.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from qgbif.qgbif import QGBIFPlugin
    return QGBIFPlugin(iface)
