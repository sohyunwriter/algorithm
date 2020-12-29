class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)-2):
            # 중복값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 기준 i 잡고, left, right 간격 좁히기
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우
                    ans.append((nums[i], nums[left], nums[right]))
                    
                    # 중복값 건너뛰기
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return ans
