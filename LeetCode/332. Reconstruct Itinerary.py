from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        route = []

        for departure, arrival in sorted(tickets): # 처음에 정렬하고 넣기
            graph[departure].append(arrival)

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))  # 맨 처음 값 계속 pop하는 식으로 구현(재방문x)
            route.append(a)

        dfs("JFK")
        return route[::-1]
