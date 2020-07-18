#
# @lc app=leetcode.cn id=518 lang=python
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        return self.helpDP(amount, coins)
        # ----------------------------------
        # res = []
        # self.dfs(amount, coins, [], 0, res, 0)
        # # print(res)
        # return len(res)

    # Solution_1 —— 动态规划
    def helpDP(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]

    # Solution_2 —— 递归(超时)
    # 打印可以凑成总金额的种类
    def dfs(self, amount, coins, path, sums, res, step):
        if sums == amount:
            res.append(path)
        for c in coins:
            if sums + c <= amount:
                if not step or path[step - 1] <= c:
                    self.dfs(amount, coins, path + [c], sums + c, res, step + 1)
        return res

# @lc code=end

