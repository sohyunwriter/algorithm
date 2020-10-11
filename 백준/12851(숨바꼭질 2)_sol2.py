# -*- coding: utf-8 -*-
import collections

N, K = map(int, input().split())

# 큐 두 개 사용
def bfs(N, K):
    visited = [0] * 100001

    # N == K일 때
    if N == K:
        return 0, 1

    q = [N] # 현재 큐
    time = 0

    while True: # 시간 1씩 증가할 때마다 다음 노드들 구하기
        nextq = [] # 다음에 등장할 노드들을 담는 큐
        nextnode = collections.defaultdict(int) # nextq에서 노드별 등장갯수
        time += 1

        # q에서 하나씩 꺼내며 다음 노드 방문
        ## 아직 방문 안 했다면 or 방문한 시간이 현재시간이라면 -> 방문하고 v에 현재시간 넣기, nextq에 삽입
        for x in q:
            for y in [x-1, x+1, x*2]:
                if 0 <= y <= 100000 and (visited[y] == 0 or visited[y] == time): # 아직 방문 안 했다면
                    nextq.append(y)
                    nextnode[y] += 1
                    visited[y] = time

        # 다음 노드에 정답 있는지 확인 (미리 확인하는게 효율적)
        if visited[K] == time:
            return time, nextnode[K]

        # 다음 노드에 정답이 없다면
        q = nextq

ans_time, ans_path = bfs(N, K)
print(ans_time)
print(ans_path)
