# 백준 16926(배열 돌리기 1) : https://www.acmicpc.net/problem/16926
# pyp3로 실행

import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1] # 우상좌하
dy = [1, 0, -1, 0]

def rotate(num):
    for i in range(0, num):
        index = 0
        x, y = i, i
        tmp = a[x][y]

        while index < 4:
            nx = x + dx[index]
            ny = y + dy[index]
            if nx >= i and ny >= i and nx < n-i and ny < m-i:
                a[x][y] = a[nx][ny]
                x = nx
                y = ny
            else:
                index += 1
        a[i+1][i] = tmp

def solve(n, m, r, a):
    num = min(n, m) // 2
    for _ in range(r):
        rotate(num)
    return a

ans = solve(n, m, r, a)
for i in ans:
    print(*i)
