from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def subset(pos, n, arr):
            if pos == n:
                return results.append(arr)

            subset(pos+1, n, arr + [nums[pos]])
            subset(pos+1, n, arr)

        subset(0, len(nums), arr=[])
        return results

sol = Solution()
print(sol.subsets(nums=[1, 2, 3]))
