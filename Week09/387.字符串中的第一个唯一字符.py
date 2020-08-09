#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        return self.helpHash(s)

    def helpHash(self, s):
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1

# @lc code=end

