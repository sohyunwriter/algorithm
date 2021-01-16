import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, pos, distance, visited, n):
    q = []

    heapq.heappush(q, (0, pos))
    distance[pos] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

def solve(n, m, pos, edges):
    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    for start, dest, cost in edges:
        graph[start].append((dest, cost))

    dijkstra(graph, pos, distance, visited, n)

    return distance

if __name__ == "__main__":
    n, m = map(int, input().split())
    pos = int(input())
    edges = [list(map(int, input().split())) for _ in range(m)]

    distance = solve(n, m, pos, edges)

    for i in range(1, n+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])
