# 문제: https://leetcode.com/problems/last-stone-weight/
# 파이썬의 내장된 heapq 모듈 이용(최소힙 -> 최대힙으로 바꿔서 사용)   

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        hq = []
        stones.sort(reverse=True)  # do sort, 44% faster -> 88% faster
        
        for i in stones:
            heapq.heappush(hq, (-i, i))
        
        while len(hq) >= 2:
            max_1 = heapq.heappop(hq)[1]
            max_2 = heapq.heappop(hq)[1]
        
            if max_1 != max_2:
                newy = max_1 - max_2
                heapq.heappush(hq, (-newy, newy))
        
        if len(hq) >= 1:
            ans = heapq.heappop(hq)[1]
        else:
            ans = 0
            
        return ans
