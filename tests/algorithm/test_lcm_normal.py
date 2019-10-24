import unittest
from src.algorithm.lcm_normal import lcm 


class TestLCM(unittest.TestCase):
    def test_GCD(self):
        a, b = 1298, 119

        actual = lcm(a, b)
        expected = 154462
        self.assertEqual(actual, expected)
