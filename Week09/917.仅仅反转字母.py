#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s_good = [ch for ch in S if ch.isalpha()]
        res = ""
        for c in S:
            res += c if not c.isalpha() else s_good.pop()
        return res

# @lc code=end

