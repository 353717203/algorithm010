#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums)

    # Solution_1 —— 动态规划
    # dp[i]表示前i个数的连续子数组的最大和
    # 前i个数的连续子数组的最大和为前i - 1个数的连续子数组的最大和加上第i个的值num[i]，
    # 如果dp[i - 1] + num[i] < num[i]，那说明dp[i - 1]对于和来说是负增益，所以应该取num[i]
    def helpDP(self, nums):
        size, res = len(nums), nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res

    # Solution_2 —— 动态规划 + 空间优化
    def helper(self, nums):
        size, res, pre = len(nums), nums[0], 0
        for i in range(0, size):
            pre = max(pre + nums[i], nums[i])
            res = max(pre, res)
        return res
# @lc code=end

