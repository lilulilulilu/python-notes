from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(matrix, start_row, end_row, start_col, end_col, target) -> bool:
            if start_row > end_row or start_col > end_col:
                return False
                
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if target == matrix[mid_row][mid_col]:
                return True

            if start_row == end_row:
                mid = (start_col + end_col) // 2
                while start_col <= mid <= end_col:
                    if target == matrix[start_row][mid]:
                        return True
                    if target > matrix[start_row][mid]:
                        start_col = mid+1
                    if target < matrix[start_row][mid]:
                        end_col = mid-1
                    mid = (start_col + end_col) // 2
                return False

            if target < matrix[mid_row][mid_col]:
                exist1 = search(matrix, mid_row, mid_row, start_col, mid_col-1, target)
                exist2 = search(matrix, start_row, mid_row-1, start_col, end_col, target)
            if target > matrix[mid_row][mid_col]:
                exist1 = search(matrix, mid_row, mid_row, mid_col+1, end_col, target)
                exist2 = search(matrix, mid_row+1, end_row, start_col, end_col, target)
            return exist1 or exist1  

        m = len(matrix)
        n = len(matrix[0])
        return search(matrix, 0, m-1, 0, n-1, target)       

print(Solution().searchMatrix([[1,3]], 3)) # True