def solve(N, t, p):
    dp = [0] * (N + 2)
    for i in range(1, N + 1):
        if (i + t[i]) <= N + 1:
            dp[i + t[i]] = max(dp[i] + p[i], dp[i + t[i]])
        dp[i + 1] = max(dp[i], dp[i + 1])
    return max(dp)


N = int(input())
t = [0] * (N + 1)
p = [0] * (N + 1)

for i in range(1, N + 1):
    ti, pi = map(int, (input().split()))
    t[i], p[i] = ti, pi

print(solve(N, t, p))
