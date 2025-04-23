import unittest
from technical_screen import *

class TestSortFunction(unittest.TestCase):

    def test_standard(self):
        # Not bulky, not heavy
        result = sort(50.0, 50.0, 50.0, 10.0)
        self.assertEqual(result, Stacks.STANDARD)

    def test_special_bulky(self):
        # Bulky, not heavy
        result = sort(200.0, 100.0, 100.0, 10.0)
        self.assertEqual(result, Stacks.SPECIAL)

    def test_special_heavy(self):
        # Heavy, not bulky
        result = sort(50.0, 50.0, 50.0, 30.0)
        self.assertEqual(result, Stacks.SPECIAL)

    def test_rejected(self):
        # Heavy and bulky
        result = sort(200.0, 200.0, 200.0, 30.0)
        self.assertEqual(result, Stacks.REJECTED)

    def test_type_validation(self):
        with self.assertRaises(AssertionError):
            sort("50", 50.0, 50.0, 10.0)

        with self.assertRaises(AssertionError):
            sort(50.0, 50, 50.0, 10.0)

        with self.assertRaises(AssertionError):
            sort(50.0, 50.0, 50.0, "10")

if __name__ == '__main__':
    unittest.main()
