## https://programmers.co.kr/learn/courses/30/lessons/60059

## 수정중(59/100)

#2차원 리스트(행렬)를 시계방향으로 90도 회전하는 메소드
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

def attach_key(x, y, key, board):
    for i in range(x, x+len(key)):
        for j in range(y, y+len(key)):
            board[i][j] += key[i-x][j-y]

def detach_key(x, y, key, board):
    for i in range(x, x+len(key)):
        for j in range(y, y+len(key)):
            board[i][j] -= key[i-x][j-y]

def check(board, key):
    for i in range(len(key) - 1, len(board) - len(key)):
        for j in range(len(key) - 1, len(board) - len(key)):
            if board[i][j] == 1:
                continue
            return False
    return True


def solution(key, lock):
    answer = True
    length = len(lock) + 2 * (len(key)-1)

    board = [[0] * length for _ in range(length)]
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            board[i+len(lock)-1][j+len(lock)-1] = lock[i][j]


    # 회전 4번
    for _ in range(4):
        for i in range(0, len(board)-len(key)+1):
            for j in range(0, len(board)-len(key)+1):
                attach_key(i, j, key, board)
                if check(board, key):
                    answer = True
                    return answer
                detach_key(i, j, key, board)
        key = rotate_a_matrix_by_90_degree(key)

    return answer

print(solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
