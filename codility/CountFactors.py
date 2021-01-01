def solution(N):
    ans = 0
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            if i*i == N:
                ans += 1
                break

            else:
                ans += 2
    
    return ans
