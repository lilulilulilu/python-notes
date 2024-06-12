import unittest
from quicksort import quicksort

class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        nums = []
        quicksort(nums)
        self.assertEqual(nums, [])

    def test_single_element_list(self):
        nums = [5]
        quicksort(nums)
        self.assertEqual(nums, [5])

    def test_two_element_list(self):
        nums = [5, 3]
        quicksort(nums)
        self.assertEqual(nums, [3, 5])

    def test_multiple_elements_list(self):
        nums = [5, 3, 9, 1, 6]
        quicksort(nums)
        self.assertEqual(nums, [1, 3, 5, 6, 9])

    def test_list_with_duplicates(self):
        nums = [5, 3, 9, 1, 6, 3, 5]
        quicksort(nums)
        self.assertEqual(nums, [1, 3, 3, 5, 5, 6, 9])

    def test_list_with_negative_numbers(self):
        nums = [5, -3, 9, 1, -6, 3, 5]
        quicksort(nums)
        self.assertEqual(nums, [-6, -3, 1, 3, 5, 5, 9])

if __name__ == '__main__':
    unittest.main()