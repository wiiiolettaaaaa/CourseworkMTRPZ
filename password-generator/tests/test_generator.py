import unittest
import sys
import os
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_only_digits(self):
        pwd = generate_password(length=10, use_digits=True, use_symbols=False, use_uppercase=False, use_lowercase=False)
        self.assertTrue(all(c in string.digits for c in pwd))

    def test_only_symbols(self):
        pwd = generate_password(length=10, use_digits=False, use_symbols=True, use_uppercase=False, use_lowercase=False)
        self.assertTrue(all(c in string.punctuation for c in pwd))

    def test_only_uppercase(self):
        pwd = generate_password(length=10, use_digits=False, use_symbols=False, use_uppercase=True, use_lowercase=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd))

    def test_only_lowercase(self):
        pwd = generate_password(length=10, use_digits=False, use_symbols=False, use_uppercase=False, use_lowercase=True)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_mixed_all(self):
        pwd = generate_password(length=30, use_digits=True, use_symbols=True, use_uppercase=True, use_lowercase=True)
        self.assertEqual(len(pwd), 30)
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))

    def test_no_characters_selected(self):
        with self.assertRaises(ValueError):
            generate_password(length=10, use_digits=False, use_symbols=False, use_uppercase=False, use_lowercase=False)

    def test_zero_length(self):
        pwd = generate_password(length=0)
        self.assertEqual(pwd, '')

if __name__ == '__main__':
    unittest.main()