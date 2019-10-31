import unittest
from src.algorithm.bsort_hard import bsort 


class TestBsort(unittest.TestCase):
    def test_bsort_cond1(self):
        actual = bsort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_bsort_cond2(self):
        actual = bsort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_bsort_cond3(self):
        actual = bsort([1, 2])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_bsort_cond4(self):
        actual = bsort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_bsort_cond5(self):
        actual = bsort([3, 2, 5, 1, 4, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_bsort_cond6(self):
        actual = bsort(["C", "CC", "B", "AA", "AD", "A"])
        expected = ["A", "AA", "AD", "B", "C", "CC"]
        self.assertEqual(actual, expected)
