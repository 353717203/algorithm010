#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.helpMerge(0, len(nums) - 1, nums)

    # Solution_1 —— 归并排序
    def helpMerge(self, l, r, nums):
        if l == r:
            return 0

        res = 0
        mid = (l + r) >> 1
        res += self.helpMerge(l, mid, nums) + self.helpMerge(mid + 1, r, nums)
        left, right = l, mid + 1
        while left <= mid and right <= r:
            if nums[left] > 2 * nums[right]:
                res += mid - left + 1
                right += 1
            else:
                left += 1
        nums[l : r + 1] = sorted(nums[l : r + 1])
        return res
        
# @lc code=end

