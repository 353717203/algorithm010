#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.help(nums)

    # Solution_1 —— 模拟
    def help(self, nums):
        maxDistance = 0
        for i, n in enumerate(nums):
            if maxDistance < i:
                return False
            else:
                maxDistance = max(i + n, maxDistance)
        return True
# @lc code=end

