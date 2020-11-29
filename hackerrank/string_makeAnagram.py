#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    mydict = defaultdict(int)
    answer = 0

    for char in a:
        mydict[char] += 1

    for char in b:
        mydict[char] -= 1

    for key, value in mydict.items():
        answer += abs(value)

    return answer

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    #fptr.write(str(res) + '\n')

    #fptr.close()
    print(res)
