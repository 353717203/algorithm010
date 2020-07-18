#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # return self.helper(prices)
        # ---------------------------
        return self.helpDP(prices)

    # Solution_1 —— 遍历
    def helper(self, prices):
        res = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
                diff = prices[i] - prices[i - 1]
                res += diff
        return res

    # Solution_2 —— 动态规划
    # dp[i][0]:表示第i天未持有股票，dp[i][1]:表示第i天持有股票
    def helpDP(self, prices):
        m = len(prices)
        dp = [[0] * 3 for _ in range(m + 1)]
        dp[0][1] = -float('inf')
        for i in range(1, m + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][0] - prices[i - 1], dp[i - 1][1])
        return dp[m][0]
# @lc code=end

