def solution(A, B, K):
    left = 0
    right = B // K

    if A % K == 0:
        left = A // K
    else:
        left =  A // K + 1

    return right - left + 1
