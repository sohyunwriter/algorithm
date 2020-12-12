#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    temp = Counter(s).most_common()

    if len(temp) == 1:
        return "YES"

    if (temp[0][1] == temp[-1][1]):
        return "YES"

    if (temp[1][1] == temp[-1][1]) and (temp[0][1] - temp[-1][1] == 1):
        return "YES"

    if (temp[0][1] == temp[-2][1]):
        if (temp[0][1] - temp[-1][1] == 1) or temp[-1][1] == 1:
            return "YES"

    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
