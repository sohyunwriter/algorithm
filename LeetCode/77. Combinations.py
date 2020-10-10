class Solution:
    def combine(self, n, k):
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])

            # 자신 이전은 이미 탐색했으니 자신 이후부터 탐색
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return results
