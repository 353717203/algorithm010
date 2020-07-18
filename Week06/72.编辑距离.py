#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # return self.helpDP(word1, word2)
        # --------------------------------
        mem = {}
        return self.dfs(word1, word2, len(word1), len(word2), mem)

    # Solution_1 —— 动态规划
    # dp[i][j]：从word1的i位置转换到word2的j位置需要的最少操作数
    # dp[i-1][j-1]：表示替换操作，将word1第i项替换为word2第j项
    # dp[i - 1][j]：表示删除操作，将word1第i项删除
    # dp[i][j - 1]：表示添加操作，将word1添加第i项
    def helpDP(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 当i = 0，表示从空串变为word2需要的最少操作数，即j添加操作
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 当j = 0，表示从空串变为word1需要的最少操作数，即i添加操作
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]

    # Solution_2 —— 记忆化搜索
    def dfs(self, word1, word2, i, j, mem = {}):
        if not i or not j:
            return i + j
        if (i, j) in mem:
            return mem[(i, j)]
        if word1[i - 1] == word2[j - 1]:
            res = self.dfs(word1, word2, i - 1, j - 1, mem)
        else:
            res = min(self.dfs(word1, word2, i - 1, j - 1, mem), 
                    self.dfs(word1, word2, i, j - 1, mem),
                    self.dfs(word1, word2, i - 1, j, mem)) + 1
        mem[(i, j)] = res
        return res
# @lc code=end

