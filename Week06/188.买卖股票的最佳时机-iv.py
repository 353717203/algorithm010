#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        return self.helpDP(k, prices)

    # Solution_1 —— 动态规划
    # dp[i][0][k]:表示第i天未持有股票,且剩余操作数未k
    # 由于买卖操作最少需要两天，所以当k > m / 2时，k没有了限制作用，等同于股票最佳时机2
    def helpDP(self, K, prices):
        m = len(prices)
        if K >= m // 2:
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    diff = prices[i] - prices[i - 1]
                    res += diff
            return res
        else:
            dp = [[[0] * 3 for _ in range(K + 1)] for _ in range(m + 1)]
            for i in range(1, m + 1):
                for k in range(K, 0, -1):
                    if i - 1 == 0:
                        dp[i][k][0] = 0
                        dp[i][k][1] = -prices[i - 1]
                        continue
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                    dp[i][k][1] = max(dp[i - 1][k - 1][0] - prices[i - 1], dp[i - 1][k][1])
            return dp[m][K][0]
# @lc code=end

