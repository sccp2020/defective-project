import unittest
from src.algorithm.two_sum import two_sum 


class TestTwoSum(unittest.TestCase):
    def test_two_sum_2(self):
        arr = [2, 7, 11, 15]
        target = 9

        actual = two_sum(arr, target)
        expected = [0, 1]
        self.assertEqual(actual, expected)

    def test_two_sum_1(self):
        arr = [0,1,2,3,4]
        target = 6

        actual = two_sum(arr, target)
        expected = [2, 4]
        self.assertEqual(actual, expected)

    def test_two_sum_3(self):
        arr = [9,3,4,5,2]
        target = 9

        actual = two_sum(arr, target)
        expected = [2, 3]
        self.assertEqual(actual, expected)
