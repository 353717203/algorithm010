#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.help(nums)

    # Solution_1 —— 贪心
    # 第一个格子为2，那么当前位置能跳以当前位置为起点的2个位置
    # 对能作为起点的2个位置区间遍历，每个格子尝试跳一次，获取能跳的最远距离
    # 跳完一次，上一次的终点作为下一次的起点，再重复遍历区间
    def help(self, nums):
        start, end, ans = 0, 1, 0
        while end < len(nums):
            maxDistance = 0
            for i in range(start, end):
                maxDistance = max(maxDistance, i + nums[i])
            start = end
            end = maxDistance + 1
            ans += 1
        return ans
# @lc code=end

