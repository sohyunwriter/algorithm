# 문제: https://programmers.co.kr/learn/courses/30/lessons/42842

def get_devision(n):
    n = int(n)
    divisors = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            if (i != (n // i)):
                divisors.append((i, n // i))
            else:
                divisors.append((i, i))
    return divisors

def solution(brown, yellow):
    divisors = get_devision(yellow)
    print(divisors)
    for i, j in divisors:
        if brown == ((i*2) + (j*2) + 4):
            return [j+2, i+2]
