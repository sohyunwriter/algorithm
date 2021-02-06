from random import randint

def points_to_star(points):
    """
    This function is to mark points(x, y) to star(*) in the board.
    Input: [(x1, y1), (x2, y2), .... ] 좌표들의 집합

    Output: 좌표는 (*)로 출력하고 아닐 경우 (.)로 출력
            단, board 크기는 (*)의 최소, 최대에 따라 이쁘게 출력. (e.g. ["...", "*.."] (<-wrong),  ["*.."] (<-correct)

    Examples:
    >>> points_to_star([(-1, 0), (1, 0)])
    ['*.*']

    >>> points_to_star([(0, 0)])
    ['*']

    >>> points_to_star([(-2, 3), (5, 4)])
    ['.......*', '*.......']
    """

    min_x = min(points, key=lambda x: x[0])[0]
    max_x = max(points, key=lambda x: x[0])[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key=lambda x: x[1])[1]
    board = [["."] * (max_x - min_x + 1) for _ in range(min_y, max_y+1)]

    # parallel translation (min_x, max_y) -> (0, 0)
    # y means row, x means col
    for x, y in points:
        board[abs(y-max_y)][x-min_x] = "*"

    ans = ["".join(i) for i in board]
    return ans

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    n = 5
    points = []
    for i in range(n):
        x = randint(-10, 10)
        y = randint(-10, 10)
        points.append([x, y])

    print(f'Question\n {points}')
    print(f'GOT\n {points_to_star(points)}')
