#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    # Solution_1 —— 回溯
    def dfs(self, nums, l, ans):
        if not nums:
            ans.append(l)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], l + [nums[i]], ans)
# @lc code=end

