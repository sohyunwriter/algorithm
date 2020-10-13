import copy

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    ncnt = 0

    for i in range(N):
        board.append(list(map(int, input().split())))

    visited = copy.deepcopy(board)
    for i in range(M):
        nowmax = max([board[j][i] for j in range(N)])
        for j in range(N):
            if board[j][i] == nowmax:
                visited[j][i] = 0

    for i in range(N):
        nowmax = max(board[i])
        for j in range(M):
            if board[i][j] == nowmax:
                visited[i][j] = 0

            if board[i][j] != nowmax and visited[i][j] != 0:
                ncnt += 1

    if ncnt == 0:
        print("#" + str(test_case) + " YES")
    else:
        print("#" + str(test_case) + " NO")
