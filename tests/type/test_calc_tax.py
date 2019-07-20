import unittest
from src.type.calc_tax import calc_tax


class TestCalcTax(unittest.TestCase):
    def test_calc_tax_eight_parcent(self):
        actual = calc_tax(1800, 1.08)
        expected = 1944
        self.assertEqual(actual, expected)

    def test_calc_tax_ten_parcent(self):
        actual = calc_tax(1800, 1.10)
        expected = 1980
        self.assertEqual(actual, expected)
