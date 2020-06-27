X, Y = input().split()

def _1120(X, Y):
    ans = 51
    for i in range(len(Y)-len(X)+1):
        count = 0
        for j, v in enumerate(X):
            if v != Y[i+j]:
                count += 1
        ans = min(ans, count)
    return ans

print(_1120(X, Y))
