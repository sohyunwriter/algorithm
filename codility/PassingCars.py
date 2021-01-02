def solution(A):
    ans = 0
    queue = []
    cursum = [0]

    for i, v in enumerate(A):
        if v == 0:
            queue.append(i)
        elif v == 1:
            cursum[-1] += 1
        
        if i != len(A)-1:
            cursum.append(cursum[-1])
    
    for i in queue:
        ans += (cursum[-1] - cursum[i])
        if ans > 1000000000:
            return -1

    return ans
