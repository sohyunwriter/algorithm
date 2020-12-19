class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회: O(N)
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]: # 딕셔너리에 없고 & 같은 게 아니면
                return nums.index(num), nums_map[target-num]
