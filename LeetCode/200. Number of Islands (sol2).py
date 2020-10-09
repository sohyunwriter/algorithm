# https://leetcode.com/problems/number-of-islands/
# Graph - DFS 이용 문제

class Solution:
    def numIslands(self, grid):
        def dfs(i, j): # dfs를 스택 이용해 구현
            # x, y 좌표 상하좌우 이동
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            stack = [(i, j)] # 초기값
            while stack:
                x, y = stack.pop()
                
                #동서남북 탐색
                for i in range(4):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    if newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0]) and grid[newx][newy] == '1': # 방문 가능하면 방문
                        stack.append((newx, newy))
                        grid[newx][newy] = '0'
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


