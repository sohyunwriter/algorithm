# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 파이썬의 sort(reverse=True) 이용

class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]
