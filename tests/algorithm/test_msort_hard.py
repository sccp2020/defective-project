import unittest
from src.algorithm.msort_hard import msort 


class TestMsort(unittest.TestCase):
    def test_msort_cond1(self):
        actual = msort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_msort_cond2(self):
        actual = msort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_msort_cond3(self):
        actual = msort([1, 2])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_msort_cond4(self):
        actual = msort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_msort_cond5(self):
        actual = msort([3, 2, 5, 1, 4, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_msort_cond6(self):
        actual = msort(["C", "CC", "B", "AA", "AD", "A"])
        expected = ["A", "AA", "AD", "B", "C", "CC"]
        self.assertEqual(actual, expected)
