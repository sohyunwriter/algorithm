from collections import defaultdict
from collections import Counter
import heapq

def dijkstra(graph, start):
    ans = 0
    INF = int(1e9)
    n = len(graph)
    dist = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        cost, node = heapq.heappop(q)
        
        if dist[node] < cost:
            continue
            
        for nextnode in graph[node]:
            nextcost = cost + 1
            if nextcost < dist[nextnode]:
                heapq.heappush(q, (nextcost, nextnode))
                dist[nextnode] = nextcost
    
    return dist

def count_maxnum(dist):
    return Counter(dist)[max(dist)]
                               
def solution(n, edge):
    # graph 만들기
    graph = defaultdict(list)
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    # 다익스트라 최단경로 및 max 반환
    answer = count_maxnum(dijkstra(graph, 1)[1:])
    
    return answer
