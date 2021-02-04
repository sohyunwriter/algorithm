# recursion with dynamic programming
# time complexity : O(N)

def solve(n: int) -> int:
    dp = [0, 1] + [-1] * (n+1)  # 0, 1 값 저장(종료조건) 및 -1로 초기화(not visited)

    def fibo(n: int) -> int:
        # 이미 방문한 노드인 경우
        if dp[n] != -1:
            return dp[n]

        # memoization하며 방문
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]

    ans = fibo(n)
    return ans

n = int(input())
print(solve(n))
