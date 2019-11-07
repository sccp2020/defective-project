import unittest
from src.algorithm.isort_hard import isort 


class TestIsort(unittest.TestCase):
    def test_isort_cond1(self):
        actual = isort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_isort_cond2(self):
        actual = isort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_isort_cond3(self):
        actual = isort([1, 2])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_isort_cond4(self):
        actual = isort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_isort_cond5(self):
        actual = isort([3, 2, 5, 1, 4, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_isort_cond6(self):
        actual = isort(["C", "CC", "B", "AA", "AD", "A"])
        expected = ["A", "AA", "AD", "B", "C", "CC"]
        self.assertEqual(actual, expected)
