import unittest
from src.type.solve_equation import solve_equation


class TestSolveEquation(unittest.TestCase):
    def test_solve_equation1(self):
        actual = solve_equation(1, 1)
        expected = -1
        self.assertEqual(actual, expected)

    def test_solve_equation2(self):
        actual = solve_equation(4, 3)
        expected = -3/4
        self.assertEqual(actual, expected)
