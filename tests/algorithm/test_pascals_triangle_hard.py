import unittest
from src.algorithm.pascals_triangle_hard import pascals_triangle


class TestPascal(unittest.TestCase):
    def test_pascal_cond_1(self):
        actual = pascals_triangle(1)
        expected = [[1]]
        self.assertEqual(actual, expected)

    def test_pascal_cond_2(self):
        actual = pascals_triangle(3)
        expected = [[1], [1, 1], [1, 2, 1]]
        self.assertEqual(actual, expected)

    def test_pascal_cond_3(self):
        actual = pascals_triangle(5)
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(actual, expected)
