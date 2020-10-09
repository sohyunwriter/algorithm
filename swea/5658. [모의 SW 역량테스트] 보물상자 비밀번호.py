# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
# 슬라이싱으로 구현

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = input()
    bnum = N // 4  # 한 변에 숫자개수
    sum = set()

    for i in range(bnum):
        for j in range(4):
            sum.add(int(num[bnum*j:bnum*(j+1)], 16))  #16진수로 바꿔 set에 추가
        num = num[-1] + num[:-1]  # 재할당

    temp = list(sum)
    temp.sort(reverse=True)
    print("#"+str(test_case)+" "+str(temp[K-1]))
