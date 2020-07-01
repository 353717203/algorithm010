#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # return self.coninDP(coins, amount)
        # ----------------------------------
        coins.sort(reverse=True)
        res = self.dfs(coins, amount, 0, 0, float('inf'))
        return res if res != float('inf') else -1

    # Solution_1 —— 动态规划
    # 需要计算总金额amount最少硬币数，可以从前一个金额的最少硬币数+1得到，类似于爬楼梯，从示例1中可知：
    # dp[11] = min(dp[11], dp[11 - 1]) + 1 
    # dp[11] = min(dp[11], dp[11 - 2]) + 1
    # dp[11] = min(dp[11], dp[11 - 5]) + 1
    # 递推公式:dp[i] = min(dp[amount - coint[j]] + 1, dp[i])
    def coninDP(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # Solution_2 —— DFS + 剪枝
    # 想要凑成总金额最少，优先用coins面值大的开始放，最多放k = amount // max(coins)个
    # 如果往下无法凑到amount，回溯减少k个数
    def dfs(self, coins, amount, index, count, ans):
        # 凑成总金额amount
        if amount == 0: return min(count, ans)
        if index == len(coins):  return ans

        k = amount // coins[index]
        # 剪枝:k + count < ans, 最少的k加上已用硬币数大于ans, 则后续无法满足最少硬币, 中止深搜
        while k >= 0 and k + count < ans:
            ans = self.dfs(coins, amount - k * coins[index], index + 1, count + k, ans)
            k -= 1
        return ans
# @lc code=end

