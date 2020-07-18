#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.helpDP(m, n)

    # Soultion_1 —— 动态规划（自底向上）
    def downupDP(self, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

    # Solution_2 —— 动态规划（自顶向下）
    def updownDP(self, m, n):
        # 初始化边界为 1
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # Solution_3 —— 动态规划 + 状态压缩
    def helpDP(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
# @lc code=end

