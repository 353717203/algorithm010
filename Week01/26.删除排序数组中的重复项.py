#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        k = 0
        for i in xrange(l):
            if nums[i] != nums[k]:
                nums[k+1] = nums[i]
                k += 1
        return k + 1
# @lc code=end

