class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        start = -1
        i = 0
        while i < n:
            if gas[i] < cost[i]:
                i = i + 1
            # 找到一个能当起始点的元素，看能不能饶完一圈
            elif gas[i] >= cost[i]:
                # take i as the start, try to find a cirle
                start = i
                j = i
                step = 0
                tank = gas[j]
                while step < n:
                    # 如果去不了下一站，就从下一个站点开始
                    if tank < cost[j]:
                        i = (j + 1) % n
                        # 如果绕完了一圈，则表示所有节点作为起始节点都没法绕完一圈
                        if i <= start:
                            return -1
                        break
                    # 如果能个去下一站，计算到达下一站后，下一次出发油箱还有多少油
                    tank = tank - cost[j] + gas[(j+1)%n]
                    step = step + 1
                    j = (j + 1)%n
                # 如果已经走了n步，
                if step >= n:
                    return start
            

        return -1

                   
Solution().canCompleteCircuit([2,3,4], [3,4,3])