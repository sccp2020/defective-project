import unittest
from src.algorithm.gcd_normal import gcd 


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        a, b = 1071, 1029

        actual = gcd(a, b)
        expected = 21 
        self.assertEqual(actual, expected)
