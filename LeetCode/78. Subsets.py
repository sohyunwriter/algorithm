class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        def dfs(nums, k, pos, subsets=[]):
            if k == 0:
                results.append(subsets[:])
                return
            
            for i in range(pos, len(nums)):
                subsets.append(nums[i])
                dfs(nums, k-1, i+1, subsets)
                subsets.pop()
        
        for i in range(len(nums)+1):
            dfs(nums, i, 0, [])
       
        return results
