import unittest
from src.crypto.base64_normal import base64


class TestBase64(unittest.TestCase):
    def test_base64_cond1(self):
        actual = base("HOGE")
        expected = "SE9HRQo="
        self.assertEqual(actual, expected)

    def test_base64_cond2(self):
        actual = caesar("Python, Ruby, Perl")
        expected = "UHl0aG9uLCBSdWJ5LCBQZXJs"
        self.assertEqual(actual, expected)

    def test_base64_cond3(self):
        actual = caesar("uzimaru = niwatori")
        expected = "dXppbWFydSA9IG5pd2F0b3Jp"
        self.assertEqual(actual, expected)
