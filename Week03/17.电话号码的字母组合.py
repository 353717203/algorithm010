#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        res = []
        # self.dfs(0, digits, '', res)
        res = self.letter(digits)
        return res

    # Solution_1 —— 递归调用
    def dfs(self, index, digits, s, ans):
        if index == len(digits):
            ans.append(s)
            return 
        for c in dic[digits[index]]:
            self.dfs(index + 1, digits, s + c, ans)

    # Solution_2 —— 暴力
    def letter(self, digits):
        s = ['']
        for c in digits:
            s = [i + j for i in s for j in dic[c]]
        return s

# @lc code=end

