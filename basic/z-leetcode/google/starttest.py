import pytest
from bs import Solution

class TestSolution:
    def setup(self):
        self.solution = Solution()
        
    def test_find_start_index_less_than_smallest(self):
        self.solution.arr = [[2, 5], [9, 13]]
        assert self.solution.find_start_index(1) == 0

    def test_find_start_index_greater_than_largest(self):
        self.solution.arr = [[2, 5], [9, 13]]
        assert self.solution.find_start_index(15) == 1

    def test_find_start_index_equal_to_start(self):
        self.solution.arr = [[2, 5], [9, 13]]
        assert self.solution.find_start_index(2) == 0
        assert self.solution.find_start_index(9) == 1

    def test_find_start_index_within_range(self):
        self.solution.arr = [[2, 5], [9, 13]]
        assert self.solution.find_start_index(3) == 0
        assert self.solution.find_start_index(10) == 1
    
    def test_find_start_index_within_range2(self):
        self.solution.arr = [[2, 5], [9, 13], [15, 20]]
        assert self.solution.find_start_index(5) == 0
        assert self.solution.find_start_index(13) == 1