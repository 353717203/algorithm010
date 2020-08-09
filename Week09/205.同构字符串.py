#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.help(s, t)
        
    def help(self, s, t):
        mapping = dict()
        used = set()
        for i, char in enumerate(s):
            if char not in mapping and t[i] not in used:
                mapping[char] = t[i]
                used.add(t[i])
            elif char not in mapping or mapping[char] != t[i]:
                return False
        return True
# @lc code=end

