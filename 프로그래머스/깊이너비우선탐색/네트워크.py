from collections import defaultdict
from collections import deque

def array_to_graph(computers, n):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i+1].append(j+1)
    return graph

def bfs(graph, start, visited):
    q = deque([start])
    while q:
        pos = q.popleft()
        if visited[pos]:
            continue
        visited[pos] = True
        for nextnode in graph[pos]:
            q.append(nextnode)
    
def solution(n, computers):
    answer = 0
    graph = array_to_graph(computers, n)
    visited = [False] * (n+1)
    
    for i in range(1, n+1):
        if not visited[i]:
            bfs(graph, i, visited)
            answer += 1
        
    return answer
