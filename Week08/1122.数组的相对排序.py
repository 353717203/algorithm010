#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return self.help(arr1, arr2)

    # Solution_1 —— 排序
    def help(self, arr1, arr2):
        res, diff = [], []
        dic = {}
        for n in arr2:
            if n not in dic:
                dic[n] = 0
        
        for n in arr1:
            if n in dic:
                dic[n] += 1
            else:
                diff.append(n)
        
        diff.sort()
        for n in arr2:
            res.extend([n] * dic[n])
        
        res.extend(diff)
        return res
# @lc code=end

