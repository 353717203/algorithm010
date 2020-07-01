#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target)

    # Solution_1 —— 二分法
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # 0 ~ mid 数组升序
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:   r = mid - 1
                else:   l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:   l = mid + 1
                else:   r = mid - 1
        return -1
# @lc code=end

