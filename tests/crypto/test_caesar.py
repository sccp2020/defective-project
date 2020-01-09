import unittest
from src.crypto.caesar_easy import caesar


class TestCaesar(unittest.TestCase):
    def test_carsar_cond1(self):
        actual = caesar("HOGE", 1)
        expected = "IPHF"
        self.assertEqual(actual, expected)

    def test_carsar_cond2(self):
        actual = caesar("Python, Ruby, Perl", 13)
        expected = "Clguba, Ehol, Crey"
        self.assertEqual(actual, expected)

    def test_carsar_cond3(self):
        actual = caesar("uzimaru = niwatori", 26)
        expected = "uzimaru = niwatori"
        self.assertEqual(actual, expected)
