import functools

def mycmp(a, b):
    if (b+a) < (a+b):
        return -1
    else:
        return 1

def solution(numbers):
    s_nums = list(map(str, numbers))
    s_nums.sort(key=functools.cmp_to_key(mycmp))
    answer = str(int(''.join(s_nums)))
        
    return answer
