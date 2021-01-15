from collections import deque

def solve(n, k):
    visited = [[False] * 2 for _ in range(500001)]
    q = deque()
    q.append([n, 0])  # pos, curdepth
    visited[n][0] = True
    time = 0 # time

    while True:
        k += time
        if (k < 0 or k > 500000):
            break

        for _ in range(len(q)):
            pos, curdepth = q.popleft()
            if pos == k or visited[k][time%2] == True:
                return time

            for next_pos in [pos+1, pos-1, pos*2]:
                if next_pos >= 0 and next_pos <= 500000 and visited[next_pos][(curdepth+1)%2] == False:
                    q.append([next_pos, curdepth+1])
                    visited[next_pos][(curdepth+1)%2] = True
        time += 1

    return -1

n, k = map(int, input().split())
print(solve(n, k))
