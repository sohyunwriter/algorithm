# for문 이용해 구현
# time complexity : O(N)

def fibo(n):
    dp = [0, 1]
    for _ in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

n = int(input())
print(fibo(n))
