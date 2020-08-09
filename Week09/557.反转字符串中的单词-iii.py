#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = []
        for i in range(len(s)):
            ans.append(s[i][::-1])
        
        return ' '.join(ans)
# @lc code=end

