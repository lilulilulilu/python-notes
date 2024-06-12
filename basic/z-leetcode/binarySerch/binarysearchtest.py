import unittest
from binarysearch import binarySearch

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found(self):
        self.assertEqual(binarySearch([1, 2, 3, 4, 5], 3), 2)
        
    def test_binary_search_found2(self):
        self.assertEqual(binarySearch([1, 2, 3, 4, 5], 1), 0)
        
    def test_binary_search_found3(self):
        self.assertEqual(binarySearch([1, 2, 3, 4, 5], 5), 4)

    def test_binary_search_not_found(self):
        self.assertEqual(binarySearch([1, 2, 3, 4, 5], 6), -1)

    def test_binary_search_empty_list(self):
        self.assertEqual(binarySearch([], 1), -1)

    def test_binary_search_single_element_found(self):
        self.assertEqual(binarySearch([1], 1), 0)

    def test_binary_search_single_element_not_found(self):
        self.assertEqual(binarySearch([1], 2), -1)
    
    def test_binary_search_double_element_found(self):
        self.assertEqual(binarySearch([1, 2], 2), 1)
        

if __name__ == '__main__':
    unittest.main()