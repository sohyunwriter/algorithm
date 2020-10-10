class Solution:
    def permute(self, nums):
        answer = []
        
        # 방문할 노드(curnum) 방문 -> 다음 방문할 노드 재귀
        def dfs(curnum, visited=[]):
            visited.append(curnum)
            if len(visited) == len(nums):
                answer.append(visited[:])
                return

            for num in nums:
                if num not in visited:
                    dfs(num, visited[:])

            visited.pop()

        for num in nums:
            dfs(num)

        return answer
        
        
