#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        # self.dfs('', n, n, res)
        res = self.dp(n)
        return res

    # Solution_1 —— DFS
    def dfs(self, s, l, r, res):
        if l == 0 and r == 0:
            res.append(s)
            return 
        # 剩余左括号多于右括号,括号组合无效
        if l > r:
            return 
        if l > 0:
            self.dfs(s + '(', l - 1, r, res)
        if r > 0:
            self.dfs(s + ')', l, r - 1, res)

    # Solution_2 —— 动态规划
    # 状态转移方程：
    # dp[n] = "(" + dp[p]的所有有效组合 + ")" + [dp[q]的组合], p + q = n - 1 , p从0遍历到n-1, q则相应从n-1到0
    def dp(self, n):
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            for p in range(i):
                dp_p = dp[p]
                dp_q = dp[i - 1 - p]
                for x in dp_p:
                    for y in dp_q:
                        dp[i].append("({0}){1}".format(x, y))
        return dp[n]

# @lc code=end

