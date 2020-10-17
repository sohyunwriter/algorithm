## 종료조건을 처음 거리좌표 기반 min, max로 하면 34번째 test case에서 시간 초과 남 -> 2000, -2000 으로 수정시 full pass

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    N = int(input())
    dict = {}
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(0, N):
        x, y, w, k = map(int, input().split())
        dict[(x*2, y*2)] = [(w, k)]

    time = 0
    while dict:
        time += 1
        dict2 = {}
        for x, y in dict.keys():
            w, k = dict[x, y].pop()
            nx = x + dx[w]
            ny = y + dy[w]
            if (nx, ny) not in dict2.keys():
                dict2[(nx, ny)] = [(w, k)]
            else:
                dict2[(nx, ny)].append((w, k))

        dict3 = {}
        for x, y in dict2.keys():
            if len(dict2[(x, y)]) > 1:
                while dict2[(x, y)]:
                    w, k = dict2[(x, y)].pop()
                    ans += k
            elif len(dict2[(x, y)]) == 1:
                if x < -2000 or x > 2000 or y > 2000 or y < -2000:
                    dict2[(x, y)].pop()
                else:
                    dict3[(x, y)] = [(dict2[(x, y)].pop())]

        dict = dict3

    print("#" + str(test_case) + " " + str(ans))
