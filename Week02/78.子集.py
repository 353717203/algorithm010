#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return self.recursion(nums)
        return self.binary(nums)
    
    # Solution_1 —— 递归
    def recursion(self, nums):
        res = [[]]
        for n in nums:
            res += [cur + [n] for cur in res]
        return res

    # Solution_2 —— 二进制
    def binary(self, nums):
        res = []
        l = len(nums)
        for i in range(2 ** l):
            tmp = []
            index = l - 1
            while index >= 0:
                if i % 2:
                    tmp.append(nums[index])
                index -= 1
                i = i >> 1
            res.append(tmp)
        return res
# @lc code=end

