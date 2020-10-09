# 문제: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 풀이: dfs, 백트래킹, 중첩함수

class Solution:
    def letterCombinations(self, digits):
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []

        def dfs(now, sum):
            # 끝까지 탐색하면 백트래킹
            if now == len(digits):
                answer.append(sum[:])
                return
            
            # 입력값 자릿수 단위 반복
            for i in dict[digits[now]]:
                # 숫자에 해당하는 모든 문자열 반복
                dfs(now + 1, sum + i)
        
        # 예외처리
        if len(digits) == 0:
            return []

        dfs(0, "")

        return answer
