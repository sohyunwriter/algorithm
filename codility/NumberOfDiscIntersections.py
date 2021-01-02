def solution(A):
    temp = []
    ans, count = 0, 0

    if not A or len(A) == 1:
        return 0

    for i, v in enumerate(A):
        temp.append((i - v, 0))
        temp.append((i + v, 1))

    temp.sort(key=lambda x: (x[0], x[1]))

    for _, flag in temp:
        if not flag:
            ans += count
            count += 1
        else:
            count -= 1

        if ans > 10000000:
            return -1

    return ans
