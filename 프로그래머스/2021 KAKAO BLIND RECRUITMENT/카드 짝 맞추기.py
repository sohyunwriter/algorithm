from collections import defaultdict
from itertools import permutations
from collections import deque

def go_far(board, x, y, movex, movey):
    tempx, tempy = x, y
    while True:
        nx, ny = tempx + movex, tempy + movey
        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
            if board[nx][ny] != 0:
                return nx, ny
            else:
                tempx, tempy = nx, ny
                continue
        else:
            return tempx, tempy

def dist(board, sx, sy, ex, ey):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])
    while q:
        x, y, cost = q.popleft()
        if x == ex and y == ey:
            return cost

        for i in range(4):
            if go_far(board, x, y, dx[i], dy[i]):
                nx, ny = go_far(board, x, y, dx[i], dy[i])
                if (nx, ny) not in visited:
                    if nx == ex and ny == ey:
                        return cost + 1
                    else:
                        visited.add((nx, ny))
                        q.append((nx, ny, cost+1))

            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
                if (nx, ny) not in visited:
                    if nx == ex and ny == ey:
                        return cost + 1
                    else:
                        visited.add((nx, ny))
                        q.append((nx, ny, cost+1))

def restore(board, mydict):
    for key, values in mydict.items():
        x1, y1 = values[0][0], values[0][1]
        x2, y2 = values[1][0], values[1][1]
        board[x1][y1], board[x2][y2] = key, key

def bfs(board, order, r, c, n, mydict):
    q = deque([(r, c, -1, 0)])

    for j in range(n+2):
        iter = len(q)
        temp = mydict[order[0]]
        for i in range(iter):
            x, y, k, cost = q.popleft()
            if k == (n - 1):
                q.append((x, y, k, cost))
                break
            temp = mydict[order[k + 1]]
            ncost = dist(board, x, y, temp[0][0], temp[0][1]) + dist(board, temp[0][0], temp[0][1], temp[1][0], temp[1][1])
            ncost2 = dist(board, x, y, temp[1][0], temp[1][1]) + dist(board, temp[1][0], temp[1][1], temp[0][0], temp[0][1])
            q.append((temp[1][0], temp[1][1], k + 1, cost + ncost))
            q.append((temp[0][0], temp[0][1], k + 1, cost + ncost2))
        board[temp[0][0]][temp[0][1]] = 0
        board[temp[1][0]][temp[1][1]] = 0

    mincost = int(1e9)
    while q:
        x, y, k, cost = q.popleft()
        if cost < mincost:
            mincost = cost

    restore(board, mydict)
    return mincost


def solution(board, r, c):
    answer = int(1e9)
    mydict = defaultdict(list)

    # dictionary (key(card_num): value(card_pos))   e.g. 1 : (0, 0), (3, 2)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                mydict[board[i][j]].append([i, j])

    n = len(mydict)

    # permutations
    orders = list(permutations(mydict.keys()))

    # visit
    for order in orders:
        answer = min(answer, bfs(board, order, r, c, n, mydict))

    answer += (2*n)
    return answer
