# -*- coding: utf-8 -*-
import collections

N, K = map(int, input().split())

def bfs(N, K):
    if N == K:
        return 0, 1

    dq = collections.deque()
    dq.append((0, N))
    ans_time = 0
    ans_path = 0
    dict = {}
    dict[N] = 0

    while dq:
        time, pos = dq.popleft()
        if ans_time != 0:
            if (ans_time == time+1) and (pos-1 == K or pos+1 == K or pos*2 == K):
                ans_path += 1
            continue

        # 다음 경로가 도착점이면 큐추가 멈추고 경로 개수 세기
        if pos-1 == K or pos+1 == K or pos*2 == K:
            ans_time = time + 1
            ans_path += 1
            continue

        if (pos-1 >= 0) and (pos-1 not in dict.keys() or dict[pos-1] == time+1):
            dq.append((time+1, pos-1))
            dict[pos-1] = time+1
        if (pos+1 < 100001) and (pos+1 not in dict.keys() or dict[pos+1] == time+1):
            dq.append((time+1, pos+1))
            dict[pos+1] = time+1
        if (pos*2 < 100001) and (pos*2 not in dict.keys() or dict[pos*2] == time+1):
            dq.append((time+1, pos*2))
            dict[pos*2] = time+1

    return ans_time, ans_path

ans_time, ans_path = bfs(N, K)
print(ans_time)
print(ans_path)
