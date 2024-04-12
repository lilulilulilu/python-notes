import unittest
import sys
sys.path.insert(0, '/Users/qqli/Documents/learn/python-exam/')
from leetcode.numsofisland import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numIslands(self):
        test_cases = [
            {
                "input": [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                ],
                "output": 1
            },
            {
                "input": [
                    ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]
                ],
                "output": 3
            },
            {
                "input": [
                    ["1","0","1","1","0"],
                    ["1","0","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","1"]
                ],
                "output": 3
            },
            {
                "input": [],
                "output": 0
            }
        ]

        for case in test_cases:
            result = self.solution.numIslands(case["input"])
            self.assertEqual(result, case["output"])

if __name__ == '__main__':
    unittest.main()