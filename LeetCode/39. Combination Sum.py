## 문제: https://leetcode.com/problems/combination-sum/
## 풀이: dfs, 백트래킹

## Runtime: 32 ms, faster than 99.17% of Python online submissions for Combination Sum.
## sort candidates -> makes possible stop early

class Solution(object):
    def combinationSum(self, candidates, target):
        results = []
        
        def dfs(cur, cursum, elements, target):
            if cursum == target:
                results.append(elements[:])
                return
            
            for i in range(cur, len(candidates)):
                if (cursum+candidates[i]) > target:  # early stop (possible due to candidates is sorted, if not sorted array it gives wrong answers)
                    return
                
                elements.append(candidates[i])
                dfs(i, cursum+candidates[i], elements, target)
                elements.pop()
        
        candidates.sort()  # sort given array
        dfs(0, 0, [], target)
        
        return results
