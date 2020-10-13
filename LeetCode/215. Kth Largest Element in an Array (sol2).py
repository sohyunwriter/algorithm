# https://leetcode.com/problems/kth-largest-element-in-an-array/
# heaqp 이용(40.94%, 84ms)보다 내장된 sort 함수 이용하는게 빠름(99.84%)
# 아래는 heaqp 이용한 경우

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        hq = []
        for n in nums:
            heapq.heappush(hq, -n)
            
        for _ in range(1, k):
            print(-heapq.heappop(hq))
        
        return -heapq.heappop(hq)
