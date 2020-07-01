#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        n, m = len(grid), len(grid[0])

        land_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    land_count += 1
                    # self.dfs(grid, i, j, n, m)
                    self.bfs(grid, i, j, n, m)
        return land_count

    # Solution_1 —— DFS
    def dfs(self, grid, x, y, n, m):
        grid[x][y] = '0'

        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                self.dfs(grid, i, j, n, m)

    # Solution_2 —— BFS
    def bfs(self, grid, x, y, n, m):
        grid[x][y] = '0'
        queue = [(x, y)]
        while queue:
            row, col = queue.pop(0)
            for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                    queue.append((i, j))
                    grid[i][j] = '0'

# @lc code=end

