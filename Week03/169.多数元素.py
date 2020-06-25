#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.hashMajority(nums)
        return self.sortMajority(nums)

    # Soultion_1 —— 哈希表
    def hashMajority(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    # Soultion_2 —— 排序
    def sortMajority(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
# @lc code=end

