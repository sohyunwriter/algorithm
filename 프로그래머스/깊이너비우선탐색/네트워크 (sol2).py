def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(n, computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j]:
                continue
            visited[j] = 1
            for i in range(n):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    for i in range(n):
        if not visited[i]:
            dfs(n, computers, visited, i)
            answer += 1
    return answer
