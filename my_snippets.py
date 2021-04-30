import itertools
import math
from collections import defaultdict

# 에라토스테네스의 체: 1부터 n까지 소수를 반환해주는 함수
def erathos(n):
    """
    :param n: 숫자 n까지
    :return: 0~n까지의 array (소수: True, 소수X: False)
    """
    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

# 2차원 리스트(행렬)를 시계방향으로 90도 회전하는 메소드
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = a[r][c]

    return res
