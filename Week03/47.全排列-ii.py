#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
from collections import Counter
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # self.dfs(nums, [], res)
        # self.trackback([], Counter(nums), len(nums), res)
        nums = sorted(nums)
        self.trackback_cut([], [0] * len(nums), nums, res)
        return res

    # Solution_1 —— 递归
    def dfs(self, nums, l, ans):
        if not nums and l not in ans:
            ans.append(l)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], l + [nums[i]], ans)

    # Solution_2 —— 回溯
    def trackback(self, path, count, n, ans):
        if len(path) == n:
            ans.append(path[:])
            return 
        for i in count:
            if count[i] > 0:
                count[i] -= 1
                path.append(i)
                self.trackback(path, count, n, ans)
                path.pop()
                count[i] += 1

    # Solution_3 —— 回溯 + 剪枝
    def trackback_cut(self, path, select, nums, ans):
        if not (0 in select):
            ans.append(path[:])
            return 
        for i in range(len(nums)):
            if select[i] == 0:
                if i > 0 and select[i - 1] == 0 and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                select[i] = 1
                self.trackback_cut(path, select, nums, ans)
                path.pop()
                select[i] = 0
# @lc code=end

