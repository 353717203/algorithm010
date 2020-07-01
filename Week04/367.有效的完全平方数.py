#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        return self.binSearch(num)

    # Solution_1 —— 二分查找
    def binSearch(self, num):
        # 一个数的平方根最多不会超过该数的一半
        l, r = 1, num // 2
        while l <= r:
            mid = l + (r - l) // 2
            if num == mid * mid:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
# @lc code=end

