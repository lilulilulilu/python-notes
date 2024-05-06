class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        i = 0

        
        while i < n:
            # 如果左边不存在，则只和右边孩子比较
            if i-1 < 0:
                if i+1 < n and ratings[i] > ratings[i+1]: # 如果比右边孩子大，则比右边孩子多一个糖果
                    candy[i] = candy[i+1] + 1

            # 如果右边不存在，则只和左边孩子比较
            elif i+1 >= n:
                if i-1 >= 0 and ratings[i] > ratings[i-1]: # 如果比左边孩子大，则比左边孩子多一个糖果
                    candy[i] = 1 + candy[i-1]
                    
            # 如果左右都存在，则和左右孩子比较      
            else:
                # 如果比左右孩子都大
                if ratings[i] > max(ratings[i-1], ratings[i+1]):
                    candy[i] = max[candy[i-1], candy[i+1]] + 1
                # 如果比左孩子大，比右孩子小
                elif ratings[i] > ratings[i-1] and ratings[i] <= ratings[i+1]:
                    candy[i] = candy[i-1] + 1
                # 如果比右孩子大，比左孩子小
                elif ratings[i] > ratings[i+1] and ratings[i] <= ratings[i-1]:
                    candy[i] = candy[i+1] + 1
            
            i = i + 1

        return sum(candy)
    
print(Solution().candy([1,2,2]) )# 