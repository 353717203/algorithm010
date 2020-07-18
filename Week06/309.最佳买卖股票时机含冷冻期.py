#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        return self.helper(prices)
        
    # Solution_1 —— 动态规划
    # dp[i][0] 表示第 i 天没有持有股票
    # dp[i][1] 表示第 i 天持有股票
    def helper(self, prices):
        size = len(prices)
        dp = [[0] * 2 for _ in range(size + 1)]
        dp[0][0] = 0
        dp[0][1] = 0
        dp[1][0] = 0
        dp[1][1] = -prices[0]
        for i in range(2, size + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])
        return dp[size][0]
# @lc code=end

