import unittest
from src.algorithm.leap_year_normal import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_leap_year1(self):
        actual = is_leap_year(2020)
        self.assertTrue(actual)

    def test_leap_year2(self):
        actual = is_leap_year(2008)
        self.assertTrue(actual)

    def test_leap_year3(self):
        actual = is_leap_year(1998)
        self.assertFalse(actual)

    def test_leap_year4(self):
        actual = is_leap_year(2010)
        self.assertFalse(actual)

