def solution(A):
    temp = []
    ans = 0
    count = 0
    if not A or len(A) == 1:
        return 0

    for i, v in enumerate(A):
        temp.append((i-v, i, 0))
        temp.append((i+v, i, 1))

    temp.sort(key=lambda x: (x[0], x[2]))
    
    for p1, p2, p3 in temp:
        if not p3:
            ans += count
            count += 1
        else:
            count -= 1
        
        if ans > 10000000:
            return -1

    return ans
