import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

def dijkstra(graph, pos, distance, visited, n):
    q = []

    # 시작노드로 가기 위한 최단 경로는 0으로 설정해, 큐에 삽입
    heapq.heappush(q, (0, pos))
    distance[pos] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = distance[now] + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

def solve(n, m, pos, edges):
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    graph = [[] for i in range(n + 1)]
    # 방문한 적이 있는지 체크하는 목적의 리스트
    visited = [False] * (n + 1)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)

    # edges -> graph 만들기
    for start, dest, cost in edges:
        graph[start].append((dest, cost))

    dijkstra(graph, pos, distance, visited, n)

    # 모든 노드로 가기 위한 최단 거리
    return distance

if __name__ == "__main__":
    # 노드의 개수, 간선의 개수를 입력받기
    n, m = map(int, input().split())
    # 시작 노드 번호를 입력받기
    pos = int(input())
    edges = [list(map(int, input().split())) for _ in range(m)]

    distance = solve(n, m, pos, edges)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(1, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
