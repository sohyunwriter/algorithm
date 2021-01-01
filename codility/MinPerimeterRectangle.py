import math

def solution(N):
    for i in range(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            ans = 2 * (N//i + i)
            return ans
