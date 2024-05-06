from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        direction = 0  # 0:right 1:down 2:left 3:up
        i = 0
        j = 0 
        v = 1
        k = 0 # 第几轮
        orders = []
        while len(orders) <= m*n:
            i = k
            j = k
            righ_end = n - k
            down_end = m - k
            left_end = j - 1
            up_end = i
            if direction == 0:
                while j < righ_end:
                    orders.append(matrix[i][j])
                    if len(orders) == m*n:
                        return orders
                    j = j + 1
                direction = 1
                j = j - 1
            if direction == 1:
                i = i + 1
                while i < down_end:
                    orders.append(matrix[i][j])
                    if len(orders) == m*n:
                        return orders
                    i = i + 1
                direction = 2
                i = i - 1
            if direction == 2:
                j = j - 1
                while j > left_end:
                    orders.append(matrix[i][j])
                    if len(orders) == m*n:
                        return orders
                    j = j - 1
                direction = 3
                j = j + 1
            if direction == 3:
                i = i - 1
                while i > up_end:
                    orders.append(matrix[i][j])
                    if len(orders) == m*n:
                        return orders
                    # matrix[i][j] = v
                    v = v + 1
                    i = i - 1
                direction = 0
                i = i + 1
                j = j + 1
            k = k + 1

        return orders
    
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

            



