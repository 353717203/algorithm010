#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        return self.binSearch(x)

    # Solution_1 —— 二分查找
    def binSearch(self, x):
        # 一个数的平方根最多不会超过该数的一半
        l, r = 1, x // 2 + 1
        while l < r:
            # 取右中位数
            mid = (l + r + 1) // 2
            if mid * mid > x:
                r = mid - 1
            else:
                l = mid
        return l
# @lc code=end

