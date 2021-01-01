def divisible(mid, K, A):
    cur_sum = 0
    for i in A:
        cur_sum += i
        if cur_sum > mid:
            cur_sum = i
            K -= 1

        if K < 0:
            return False
    
    return True

def solution(K, M, A):
    min_num = 0
    max_num = 0
    ans = 0
    for i in A:
        max_num += i  
        min_num = max(min_num, i)
    ans = max_num

    while min_num <= max_num:
        mid = (min_num + max_num) // 2
        if (divisible(mid, K-1, A)):
            max_num = mid - 1
            ans = mid
        else:
            min_num = mid + 1

    return ans
