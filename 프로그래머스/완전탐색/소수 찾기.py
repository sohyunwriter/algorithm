# 문제: https://programmers.co.kr/learn/courses/30/parts/12230

import itertools
import math
from collections import defaultdict

def erathos(n):
    array = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

def solution(numbers):
    answer = 0
    mydict = defaultdict(int)
    numbers_list = list(map(int, numbers))
    max_num = int("".join(map(str, sorted(numbers_list, reverse=True))))
    array = erathos(max_num+1)

    for i in range(1, len(numbers) + 1):
        for j in itertools.permutations(numbers_list, i):
            number = int("".join(map(str, j)))
            if array[number]:
                if not mydict[number] and number not in (0, 1):
                    print(number)
                    answer += 1
                    mydict[number] = 1
    return answer

print(solution("011"))
