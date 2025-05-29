import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default(self):
        pwd = generate_password()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        self.assertEqual(len(generate_password(length=20)), 20)

    def test_error(self):
        with self.assertRaises(ValueError):
            generate_password(digits=False, symbols=False, uppercase=False)

if __name__ == '__main__':
    unittest.main()