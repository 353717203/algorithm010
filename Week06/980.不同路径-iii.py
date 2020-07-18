#
# @lc app=leetcode.cn id=980 lang=python
#
# [980] 不同路径 III
#

# @lc code=start
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        step = 0
        x = y = 0
        self.ex = self.ey = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                    step += 1
                elif grid[i][j] == 0:
                    step += 1
                elif grid[i][j] == 2:
                    self.ex, self.ey = i, j
                    step += 1
        self.res = 0
        grid[x][y] = -1
        self.dfs(grid, x, y, m, n, step, 0)
        return self.res

    def dfs(self, grid, x, y, m, n, step, cnt):
        if x == self.ex and y == self.ey:
            if step - 1 == cnt:
                self.res += 1
            return 
        
        for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] != -1:
                tmp = grid[dx][dy]
                grid[dx][dy] = -1
                self.dfs(grid, dx, dy, m, n, step, cnt + 1)
                grid[dx][dy] = tmp
# @lc code=end

