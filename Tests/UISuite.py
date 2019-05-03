import unittest

from Tests.UI.MovieListTest import MovieListTest


def suite():
    suite = unittest.TestSuite()
    suite.addTests(MovieListTest())

