# LeetCode 5. Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/
# 확장해나가기 concept

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            
        # 0글자, 1글자 (eg. "a")
        if len(s) < 2:
            return s

        for i in range(len(s)-1):
            ans = max(ans, expand(i, i), expand(i, i + 1), key=len)

        return ans
