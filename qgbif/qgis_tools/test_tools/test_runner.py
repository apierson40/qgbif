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

import unittest

from .conftest import pytest_report_header


def _run_tests(test_suite, package_name, pattern):
    """Core function to test a test suite.
    :param test_suite: Unittest test suite
    """
    count = test_suite.countTestCases()
    print("######## Environment   ########")
    print(pytest_report_header())
    print("{} tests has been discovered in {} with pattern {}".format(count, package_name, pattern))
    print("######## Running tests ########")
    results = unittest.TextTestRunner(verbosity=2).run(test_suite)
    print("######## Summary       ########")
    print("Errors               : {}".format(len(results.errors)))
    print("Failures             : {}".format(len(results.failures)))
    print("Expected failures    : {}".format(len(results.expectedFailures)))
    print("Unexpected successes : {}".format(len(results.unexpectedSuccesses)))
    print("Skip                 : {}".format(len(results.skipped)))
    successes = (
        results.testsRun - (
            len(results.errors) + len(results.failures) + len(results.expectedFailures)
            + len(results.unexpectedSuccesses) + len(results.skipped)))
    print("Successes            : {}".format(successes))
    print("TOTAL                : {}".format(results.testsRun))


def test_package(package="..", pattern="test_*.py"):
    """Test package.
    This function is called by travis without arguments.
    :param package: The package to test.
    :type package: str
    """
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover(package, pattern=pattern)
    _run_tests(test_suite, package, pattern)


if __name__ == "__main__":
    test_package()
