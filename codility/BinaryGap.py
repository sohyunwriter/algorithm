def solution(N):
    bin_num = str(bin(N)[2:])
    ans = 0
    pre_idx = 0
    for i, v in enumerate(bin_num):
        if v == '1':
            ans = max(ans, i - pre_idx - 1)
            pre_idx = i

    return ans
