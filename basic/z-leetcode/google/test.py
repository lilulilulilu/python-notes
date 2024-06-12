import unittest
from bs import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combine(self):
        self.assertEqual(self.solution.combine([1, 2], [3, 4]), [1, 4])
        self.assertEqual(self.solution.combine([3, 4], [1, 2]), [1, 4])

    def test_union(self):
        with self.assertRaises(ValueError):
            self.solution.union(2, 1)
        self.solution.union(1, 2)
        self.assertEqual(self.solution.arr, [[1, 2]])
        self.solution.union(2, 3)
        self.assertEqual(self.solution.arr, [[1, 3]])
        self.solution.union(5, 6)
        self.assertEqual(self.solution.arr, [[1, 3], [5, 6]])
        self.solution.union(0, 7)
        self.assertEqual(self.solution.arr, [[0, 7]])

    def test_find(self):
        self.solution.union(1, 2)
        self.assertTrue(self.solution.find(1))
        self.assertTrue(self.solution.find(2))
        self.assertFalse(self.solution.find(0))
        self.assertFalse(self.solution.find(3))

if __name__ == '__main__':
    unittest.main()