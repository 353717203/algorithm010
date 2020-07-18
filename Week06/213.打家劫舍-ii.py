#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.helpDP(nums[:-1]), self.helpDP(nums[1:]))

    # Solution_1 —— 动态规划 + 空间优化
    # 和前一个不同的是，这次的房屋是环形的,只需要去头尾各计算一次
    # 当偷了num[0],则不能偷num[n - 1],当没偷num[0],则可以偷num[n - 1]
    # 因此能偷取最高的金额就是max(num[0:n-1], num[1:n])
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    # prev = dp[i - 1], curr = dp[i - 2]
    def helpDP(self, nums):
        prev, curr = 0, 0
        for i in range(len(nums)):
            prev, curr = max(curr + nums[i], prev), prev
        return prev
# @lc code=end

