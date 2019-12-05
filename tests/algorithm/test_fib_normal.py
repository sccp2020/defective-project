import unittest
from src.algorithm.fib_normal import fib 


class TestFib(unittest.TestCase):
    def test_fib_cond_1(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_fib_cond_2(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_fib_cond_3(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_fib_cond_4(self):
        actual = fib(7)
        expected = 13
        self.assertEqual(actual, expected)
