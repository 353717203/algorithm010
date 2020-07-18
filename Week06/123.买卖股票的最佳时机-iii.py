#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.helpDP(prices)

    # Solution_1 —— 动态规划
    # dp[i][0][k]:表示第i天未持有股票,且剩余操作数未k
    def helpDP(self, prices):
        m, K = len(prices), 2
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for k in range(K, 0, -1):
                if i - 1 == 0:
                    dp[i][0][k] = 0
                    dp[i][1][k] = -prices[i - 1]
                    continue
                dp[i][0][k] = max(dp[i - 1][0][k], dp[i - 1][1][k] + prices[i - 1])
                dp[i][1][k] = max(dp[i - 1][0][k - 1] - prices[i - 1], dp[i - 1][1][k])
        return dp[m][0][K]
# @lc code=end

