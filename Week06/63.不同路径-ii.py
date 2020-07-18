#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 起点or终点有障碍
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        return self.helpDP(obstacleGrid)

    # Solution_1 —— 动态规划(自顶向下)
    def updownDP(self, arr, m, n):
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if arr[i][j]:
                    continue
                if not i and not j:
                    dp[i][j] = 1
                    continue
                if i:
                    dp[i][j] += dp[i - 1][j]
                if j:
                    dp[i][j] += dp[i][j - 1]
                    
        return dp[m - 1][n - 1]

    # Solution_2 —— 动态规划(自底向上)
    def downupDP(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

    # Solution_3 —— 动态规划 + 状态压缩
    def helpDP(self, arr):
        m, n = len(arr), len(arr[0]) 
        dp = [1] + [0] * (n - 1)
        for i in range(m):
            for j in range(n):
                if arr[i][j]:
                    dp[j] = 0
                    continue
                if j:
                    dp[j] += dp[j - 1]
        return dp[-1]
                
# @lc code=end

