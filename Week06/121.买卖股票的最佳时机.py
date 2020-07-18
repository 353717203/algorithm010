#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.helpDP(prices)

    # Solution_1 —— 遍历
    def helper(self, prices):
        if not prices:
            return 0
        min_num, res = prices[0], 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_num)
            min_num = min(min_num, prices[i])
        return res

    # Solution_2 —— 动态规划
    # dp[i][0]:表示第i天未持有股票，dp[i][1]:表示第i天持有股票
    def helpDP(self, prices):
        m = len(prices)
        # dp[0][0]第0天还未开始，利润为0， dp[0][1]第0天未开始，不可能持有股票，负无穷
        dp = [[0] * 3 for _ in range(m + 1)]
        dp[0][1] = -float('inf')
        for i in range(1, m + 1):
            # i - 1天未持有股票 or i - 1天持有股票，i天卖出
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            # i - 1天未持有股票，卖出 or i - 1天持有股票
            dp[i][1] = max(-prices[i - 1], dp[i - 1][1])
        return dp[m][0] 

# @lc code=end

