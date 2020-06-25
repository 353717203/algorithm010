#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        res = []
        self.trackback(1, [], n, k, res)
        return res

    # Solution_1 —— 回溯
    def trackback(self, index, path, n, k, ans):
        if len(path) == k:
            ans.append(path[:])
            return 
        for i in range(index, n + 1):
            path.append(i)
            self.trackback(i + 1, path, n, k, ans)
            path.pop()
# @lc code=end

