import sys
input = sys.stdin.readline

def count_connected_component(n, graph):
    cnt = 0
    visited = [False] * (n+1)

    def dfs(graph, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j]:
                continue

            visited[j] = True

            for i in graph[j]:
                if not visited[i]:
                    stack.append(i)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, visited, i)
            cnt += 1
    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())

    # make graph
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # count connected component
    answer = count_connected_component(n, graph)

    print(answer)
