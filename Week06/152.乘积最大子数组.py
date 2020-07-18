#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.helpDP(nums)
        # -------------------------
        # return self.optimizeDP(nums)
        # -------------------------
        return self.math(nums)

    # Solution_1 —— 动态规划
    # 和最大子数组的和不一样，乘积时最大正数乘上负数会变成最小值，最小负数乘上负数会变成最大值
    # 因此这里需要记录两个变量，最大值和最小值
    def helpDP(self, nums):
        n, res = len(nums), nums[0]
        max_dp = [nums[0]] + [0] * (n - 1)
        min_dp = [nums[0]] + [0] * (n - 1)
        
        for i in range(1, n):
            max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(min_dp[i - 1] * nums[i], nums[i], max_dp[i - 1] * nums[i])
            res = max(res, max_dp[i])
        return res
    
    # Solution_2 —— 动态规划 + 空间优化
    # 当num[i]为负数时，会导致最大正数变最小数，最小数变成最大正数
    # 因此在num[i]为负数时，先交换最大值和最小值
    def optimizeDP(self, nums):
        n, res = len(nums), -float('inf')
        max_dp = min_dp = 1
        for i in range(n):
            if nums[i] < 0:
                min_dp, max_dp = max_dp, min_dp
            max_dp = max(max_dp * nums[i], nums[i])
            min_dp = min(min_dp * nums[i], nums[i])
            res = max(max_dp, res)
        return res

    # Solution_3 —— 分类讨论
    # num值全为正数(不含0)：直接相乘为最大乘积
    # num值有偶数个负数(不含0)：直接相乘为最大乘积
    # num值为奇数个负数(不含0)：分别从左往右乘和从右往左乘计算，到最后一个负数中止，
    #                      则之前的负数个数为偶数，取从左往右和从右往左的最大值为最大乘积
    # num值为0时，由于是乘法，不管后面数多大乘积都为0，因此下一个值从自身开始往后乘
    def math(self, nums):
        n = len(nums)
        reverse_nums = nums[::-1]
        for i in range(1, n):
            # 如果num[i-1]为0，那么num[i]从自身开始计算
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(max(nums), max(reverse_nums))
# @lc code=end

