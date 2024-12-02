# test_app.py
import unittest
from app import add_numbers, subtract_numbers

class TestCalculator(unittest.TestCase):
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 2), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
    
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(3, 3), 0)
        self.assertEqual(subtract_numbers(-1, 1), -2)

if __name__ == '__main__':
    unittest.main()

