from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        route = []

        for departure, arrival in sorted(tickets): 
            graph[departure].append(arrival)

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs("JFK")
        return route[::-1]
