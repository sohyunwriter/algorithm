import sys
#f = open("output.txt", "r")
#lines = f.read().splitlines()
#f.close()
#sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    width = int(input())
    hlist = list(map(int, input().split()))
    answer = 0
    for i in range(2, width-2):
        left = hlist[i] - max(hlist[i-1], hlist[i-2])
        right = hlist[i] - max(hlist[i+1], hlist[i+2])
        if left > 0 and right > 0:
            answer += min(left, right)

    print("#" + str(test_case) + " " + str(answer))

    '''
    if lines[test_case-1] == "#" + str(test_case) + " " + str(answer):
        print("true")
    else:
        print("false")
    '''
