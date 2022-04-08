import unittest
from arrays_and_strings import is_unique


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_unique('aaaa'), False)  # add assertion here
        self.assertEqual(is_unique('abcde'), True)  # add assertion here
        self.assertEqual(is_unique('abcda'), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
