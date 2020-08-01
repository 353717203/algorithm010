#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.helpSort(intervals)

    # Solution_1 —— 排序
    # 将数据按照左边界升序排序，如果当前区间的左边界大于上一个区间的右边界，则直接将数据添加到res
    # 如果当前区间的左边界小于等于上一个区间的右边界，则将区间合并，取两个中较大的右边界
    def helpSort(self, intervals):
        intervals.sort(key = lambda x : x[0])
        res = []
        for num in intervals:
            if not res or res[-1][1] < num[0]:
                res.append(num)
            else:
                res[-1][1] = max(res[-1][1], num[1])
        return res
# @lc code=end

