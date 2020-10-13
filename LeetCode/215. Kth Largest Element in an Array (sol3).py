# list -> heapify -> for: len(nums)-k
# still slow (48.93% faster)

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
            
        return heapq.heappop(nums)
