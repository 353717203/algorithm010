#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        for i in range(l - 1, -1, -1):
            if (digits[i] != 9):
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
# @lc code=end

