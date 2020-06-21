#
# app=leetcode.cn id=49 lang=python
#
# [面试49] 丑数
# code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.uglyNumber(n)
    
    # Solution_1 —— 动态规划
    def uglyNumber(self, n):
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            num_2, num_3, num_5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(num_2, num_3, num_5)
            if dp[i] == num_2: a += 1
            if dp[i] == num_3: b += 1
            if dp[i] == num_5: c += 1
        return dp[-1]
# code=end