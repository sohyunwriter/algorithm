# graph 순환구조 판단 문제 (64ms)
from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph = defaultdict(list)
        visited = [False]*numCourses
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(num):
            if visited[num] == True:
                return False
                        
            visited[num] = True
            
            while graph[num]:
                if not dfs(graph[num].pop()):
                    return False
            
            visited[num] = False
            
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
