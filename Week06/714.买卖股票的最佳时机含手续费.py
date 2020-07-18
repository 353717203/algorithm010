#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        return self.helpDP(prices, fee)
        
    # Solution_1 —— 动态规划
    def helpDP(self, prices, fee):
        m = len(prices)
        dp_0, dp_1 = 0, -float('inf')
        for i in range(1, m + 1):
            dp_0 = max(dp_0, dp_1 + prices[i - 1] - fee)
            dp_1 = max(dp_0 - prices[i - 1], dp_1)
        return dp_0
# @lc code=end

