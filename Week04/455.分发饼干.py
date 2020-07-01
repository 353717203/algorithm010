#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        return self.pointer(g, s)
        
    # Solution_1 —— 双指针
    def pointer(self, g, s):
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                res += 1
            j += 1
        return res
# @lc code=end

