#
# @lc app=leetcode.cn id=1091 lang=python
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        elif n <= 2:
            return n

        return self.bfs(grid, n)
        
    # Solution_1 —— BFS
    def bfs(self, grid, n):
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        while queue:
            x, y, step = queue.pop(0)
            for i, j in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                dx, dy = x + i, y + j
                if dx == n - 1 and dy == n - 1:
                    return step + 1
                if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 0:
                    queue.append((dx, dy, step + 1))
                    grid[dx][dy] = 1
        return -1
# @lc code=end

