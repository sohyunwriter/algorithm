# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE
# 풀이: 구현 (무조건 숫자 횟수에 맞춰 바꿔야 하므로, 큰 수에 도달했는데 횟수가 남은 경우 조건 처리 주의)

T = int(input())
answer = [0]

def dfs(start, cnt, k, temp):
    # end 조건
    if cnt == k: 
        if answer[0] < int(''.join(list(map(str, temp)))):
            answer[0] = int(''.join(list(map(str, temp))))
        return

    if start >= len(temp)-1:
        if (k - cnt) % 2 == 0 or len(temp) != len(set(temp)):
            #print("sssss")
            if (answer[0] < int(''.join(list(map(str, temp))))):
                answer[0] = int(''.join(list(map(str, temp))))
        else:
            #print("here")
            temp_after = temp.copy()
            temp_after[-1], temp_after[-2] = temp_after[-2], temp_after[-1]
            if (answer[0] < int(''.join(list(map(str, temp_after))))):
                answer[0] = int(''.join(list(map(str, temp_after))))
        return

    # 바꿀 수 있는 경우의 수
    curmax = max(temp[start:])
    if temp[start] == curmax:
        dfs(start+1, cnt, k, temp)
    else:
        spos = []
        for i in range(start+1, len(num)):
            if temp[i] == curmax:
                spos.append(i)

        for i in spos:
            temp_after = temp.copy()
            temp_after[start], temp_after[i] = temp_after[i], temp_after[start]
            dfs(start+1, cnt+1, k, temp_after[:])


for test_case in range(1, T + 1):
    num, k = input().split()  # string
    temp = []
    for i in num:
        temp.append(int(i))

    dfs(0, 0, int(k), temp[:])
    print("#" + str(test_case) + " " + str(answer[0]))

    answer = [0]

