#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Solution_1 —— 排序 + 数组分类
        # -----------------------------
        # dic = {}
        # for s in strs:
        #     keys = "".join(tuple(sorted(s)))
        #     if keys not in dic:
        #         dic[keys] = [s]
        #     else:
        #         dic[keys].append(s)
        # return list(dic.values())

        # Solution_2 —— 排序 + 数组分类
        # -----------------------------
        # dic = collections.defaultdict(list)
        # for s in strs:
        #     dic[tuple(sorted(s))].append(s)
        # return dic.values()

        # Solution_3 —— 计数分类
        # -----------------------------
        dic = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)].append(s)
        return dic.values()
# @lc code=end

