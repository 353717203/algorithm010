#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.helpDP(text1, text2)

    # Solution_1 —— 动态规划
    # 当字符text1[-1] == text2[-1]：
    # 相当于求l1 - 1长度的text1串和l2 - 1长度的text2串的最长公共子序列
    # 当字符text1[-1] != text2[-1]：
    # 相当于求子问题最大：l1 - 1长度的text1串和text2相比，l2 - 1长度的text2串和text1相比
    def helpDP(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

# @lc code=end

