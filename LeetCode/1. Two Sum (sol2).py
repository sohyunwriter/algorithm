class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # in을 이용한 탐색 O(N^2)
        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums[i+1:]:
                return nums.index(num), nums[i+1:].index(complement) + (i+1)
