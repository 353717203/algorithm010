#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helpDP(n)
        # return self.bfs(n)

    # Solution_1 —— 动态规划
    # dp[i]：组成正整数i的最少完全平方数
    def helpDP(self, n):
        squares = [i * i for i in range(0, int(n ** 0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for k in squares:
                if k > i:
                    break
                dp[i] = min(dp[i], dp[i - k] + 1)
        return dp[-1]

    # Solution_2 —— BFS
    def bfs(self, n):
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        visited = set()
        queue = [(n, 0)]
        while queue:
            num, step = queue.pop(0)
            if num == 0:
                return step
            for k in squares:
                if num - k not in visited:
                    queue.append((num - k, step + 1))
                    visited.add(num - k)
        return 0

# @lc code=end

