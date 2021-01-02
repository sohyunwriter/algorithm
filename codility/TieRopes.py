def solution(K, A):
    ans, cursum = 0, 0

    for i in A:
        if (i >= K) or (cursum + i >= K):
            ans += 1
            cursum = 0
        else:
            cursum += i

    return ans
