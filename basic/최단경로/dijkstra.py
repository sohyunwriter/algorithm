'''
# dijkstra algorithm without priorityQueue
# time complexity : O(V^2)
# space complexity : O(V+E)
'''

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# edges -> graph 만들기: O(E)
def edges2graph(edges, n):
    graph = [[] for i in range(n+1)]  # sc: O(V)
    for start, dest, cost in edges:  # tc: O(E)
        graph[start].append((dest, cost))
    return graph

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환 : O(V)
def get_smallest_node(distance, visited):
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘 : O(V^2)
def dijkstra(graph, pos, n):
    # 방문한 적이 있는지 체크하는 목적의 리스트 # sc: O(V)
    visited = [False] * (n + 1)

    # 최단 거리 테이블을 모두 무한으로 초기화 # sc: O(V)
    distance = [INF] * (n + 1)

    # 시작 노드에 대해서 초기화
    distance[pos] = 0
    visited[pos] = True
    for j in graph[pos]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복 : O(V^2)
    for i in range(n-1):  # tc: O(V)
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node(distance, visited) # tc: O(V)
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인 # O(V) (node-node 간 중복된 edge가 있으면 O(E))
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

    return distance

def solve(n, m, pos, edges):
    # edges -> graph
    graph = edges2graph(edges, n)
    # dijkstra
    distance = dijkstra(graph, pos, n)  # 그래프, 시작위치,노드 개수
    # 모든 노드로 가기 위한 최단 거리 반환
    return distance

if __name__ == "__main__":
    # 노드의 개수, 간선의 개수를 입력받기
    n, m = map(int, input().split())
    # 시작 노드 번호를 입력받기
    pos = int(input())
    # 간선 정보 입력받기
    edges = [list(map(int, input().split())) for _ in range(m)]  # sc: O(E)

    distance = solve(n, m, pos, edges)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(1, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
