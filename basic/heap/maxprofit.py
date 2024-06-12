from heapq import heappop, heappush
from typing import List

class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nxts = []
        heappush(nxts, (nums1[0]+nums2[0], (0,0)))
        visited = set() # add to nxts
        visited.add((u,v))
        results = []
        m = len(nums1)
        n = len(nums2)
        while nxts and k > 0:
            s, uv = heappop(nxts)
            u,v = uv
            results.append([nums1[u], nums2[v]])
            k = k-1
            if u+1 < m and (u+1,v) not in visited:
                heappush(nxts,(nums1[u+1]+nums2[v], (u+1,v)))
            if v+1 < n and (u,v+1) not in visited:
                heappush(nxts,(nums1[u]+nums2[v+1], (u,v+1)))
        return results
    
print(Solution().kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20)) # [[1,2],[1,4],[1,6]]