from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        route = []

        for departure, arrival in sorted(tickets, reverse=True):  # 역순 정렬(pop() 써서 O(1)으로 풀기 위해)
            graph[departure].append(arrival)

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs("JFK")
        return route[::-1]
