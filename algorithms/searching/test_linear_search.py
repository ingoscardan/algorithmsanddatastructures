import unittest
from random import shuffle
from linear_search import linear_search_iterative


class MyTestCase(unittest.TestCase):
    def test_element_not_found(self):
        """Element not found in the list"""
        list_elements = [*range(100)]  # * use to unpack the range list
        shuffle(list_elements)
        self.assertEqual(linear_search_iterative(list_elements, 105), -1)
        try:
            result = list_elements.index(105)
        except ValueError:
            result = -1
        self.assertEqual(linear_search_iterative(list_elements, 105), result)


if __name__ == '__main__':
    unittest.main()
