#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from collections import Counter

def substrCount(n, s):
    l = []
    count = 0
    cur = None

    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    answer = 0
    for i in l:
        answer += ((i[1] * (i[1]+1)) // 2)

    for i in range(1, len(l)-1):
        if l[i-1][0] == l[i+1][0] and l[i][1] == 1:
            answer += min(l[i-1][1], l[i+1][1])
    return answer
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
