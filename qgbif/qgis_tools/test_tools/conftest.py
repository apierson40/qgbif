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

import sys

from osgeo import gdal
from qgis.PyQt import Qt
from qgis.core import Qgis


def pytest_report_header():
    """Used by PyTest and Unittest."""
    message = "QGIS : {}\n".format(Qgis.QGIS_VERSION_INT)
    message += "Python GDAL : {}\n".format(gdal.VersionInfo("VERSION_NUM"))
    message += "Python : {}\n".format(sys.version)
    message += "QT : {}".format(Qt.QT_VERSION_STR)
    return message
