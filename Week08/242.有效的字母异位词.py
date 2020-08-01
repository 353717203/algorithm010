#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.helpHash(s, t)
        # ----------------------------
        # return self.helpSet(s, t)
        # ----------------------------
        # return Counter(s) == Counter(t)
        # ----------------------------
        # return sorted(s) == sorted(t)

    # Solution_1 —— set去重
    def helpSet(self, s, t):
        if len(s) != len(t):
            return False
        s_set = set(s)
        for c in s_set:
            if s.count(c) != t.count(c):
                return False
        return True

    # Solution_2 —— 哈希表
    def helpHash(self, s, t):
        if len(s) != len(t):
            return False
        dic = collections.defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1
            dic[t[i]] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        return True
# @lc code=end

