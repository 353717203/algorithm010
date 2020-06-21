#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return self.kFrequent(nums, k)
    
    # Solution_1 —— 堆(小顶堆)
    def kFrequent(self, nums, k):
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        print(dic)
        return heapq.nlargest(k, dic.keys(), key=dic.get)
# @lc code=end

