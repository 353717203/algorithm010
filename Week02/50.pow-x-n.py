#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        # return self.recursion(x, n) if n > 0 else 1.0 / self.recursion(x, -n)
        return self.iteration(x, n) if n > 0 else 1.0 / self.iteration(x, -n)

    # Solution_1 —— 递归
    def recursion(self, x, n):
        if n == 0:
            return 1.0
        mid = self.recursion(x, n // 2)
        return mid * mid if n % 2 == 0 else mid * mid * x

    # Solution_2 —— 迭代
    def iteration(self, x, n):
        res = 1.0
        k = x
        while n > 0:
            if n % 2 == 1:
                res *= k
            k *= k
            n //= 2
        return res
# @lc code=end

