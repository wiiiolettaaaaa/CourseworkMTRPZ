import unittest
import sys
import os
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def default_args(self):
        return {
            'length': 12,
            'use_digits': True,
            'use_symbols': True,
            'use_uppercase': True,
            'use_lowercase': True,
        }

    def test_default(self):
        args = self.default_args()
        pwd = generate_password(**args)
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        args = self.default_args()
        args['length'] = 20
        pwd = generate_password(**args)
        self.assertEqual(len(pwd), 20)

    def test_only_digits(self):
        pwd = generate_password(10, use_digits=True, use_symbols=False, use_uppercase=False, use_lowercase=False)
        self.assertTrue(all(c in string.digits for c in pwd))

    def test_only_symbols(self):
        pwd = generate_password(10, use_digits=False, use_symbols=True, use_uppercase=False, use_lowercase=False)
        self.assertTrue(all(c in string.punctuation for c in pwd))

    def test_only_uppercase(self):
        pwd = generate_password(10, use_digits=False, use_symbols=False, use_uppercase=True, use_lowercase=False)
        self.assertTrue(all(c in string.ascii_uppercase for c in pwd))

    def test_only_lowercase(self):
        pwd = generate_password(10, use_digits=False, use_symbols=False, use_uppercase=False, use_lowercase=True)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_mixed_all(self):
        args = self.default_args()
        pwd = generate_password(**args)
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))
        self.assertTrue(any(c in string.ascii_uppercase for c in pwd))
        self.assertTrue(any(c in string.ascii_lowercase for c in pwd))

    def test_error(self):
        with self.assertRaises(ValueError):
            generate_password(12, use_digits=False, use_symbols=False, use_uppercase=False, use_lowercase=False)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_password(0, use_digits=True, use_symbols=False, use_uppercase=False, use_lowercase=False)

if __name__ == '__main__':
    unittest.main()