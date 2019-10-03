import unittest
from src.type.solve_equation import solve_equation


class TestCompareLength(unittest.TestCase):
    def test_compare_length_cond1(self):
        actual = solve_equation(1, 1)
        expected = -1
        self.assertEqual(actual, expected)

    def test_compare_length_cond2(self):
        actual = solve_equation(4, 3)
        expected = -3/4
        self.assertEqual(actual, expected)
