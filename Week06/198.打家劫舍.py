#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    
            return 0
        # return self.helpDP(nums)
        # ------------------------
        return self.help(nums)

    # Solution_1 —— 动态规划
    # dp[i]:表示前i天偷窃到的最高金额
    def helpDP(self, nums):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        return dp[n]

    # Solution_2 —— 动态规划 + 空间优化
    # prev = dp[i - 1], curr = dp[i - 2]
    def help(self, nums):
        prev, curr = 0, 0
        for i in range(len(nums)):
            prev, curr = max(curr + nums[i], prev), prev
        return prev

# @lc code=end

