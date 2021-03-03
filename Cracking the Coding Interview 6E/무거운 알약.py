from random import randint

"""
This code is simulation code of below question.

Q. 무거운 알약: 
약병 20개가 있다. 
이 중 19개에는 1.0그램짜리 알약들이 들어있고, 하나에는 1.1그램짜리 알약들이 들어 있다. 
정확한 저울 하나가 주어졌을 때, 무거운 약병을 찾으려면 어떻게 해야 할까? 
저울은 딱 한 번만 쓸 수 있다.
"""

def simul(n, data):
    total = 0
    for i in range(1, n+1):
        total += data[i] * i
    return total

def solve(n, data):
    # return int((simul(n, data) - int(n*(n+1)//2)) / 0.1)
    return int(round(simul(n, data) - int(n*(n+1)//2), 2) * 10)   # 수식: (전체 무게 - 210) / 0.1

if __name__ == "__main__":
    # make data
    n = 20
    data = [1]*(n+1)
    expected = randint(1, 20)
    data[expected] = 1.1

    # answer
    actual = solve(n, data)
    print(data)
    print(f'Expected: {expected}\nActual: {actual}')
    assert expected == actual
