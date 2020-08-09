#
# @lc app=leetcode.cn id=44 lang=python
#
# [44] 通配符匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        return self.helpBack(s, p, m, n)

    # Solution_1 —— 动态规划
    def helpDp(self, s, p, m, n):
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 当字符串s为空时，p的前i个字母为*时，才为真，此时*表示空字符串
        for i in range(1, n + 1):
            if p[i - 1] != '*': break
            dp[0][i] = True
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[m][n]

    # Solution_2 —— 回溯
    def helpBack(self, s, p, m, n):
        i, j, iStar, jStar = 0, 0, -1, -1
        while i < m:
            if j < n and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                iStar, jStar = i, j
                j += 1
            elif iStar >= 0:
                iStar += 1
                i = iStar
                j = jStar + 1
            else:
                return False

        while j < n and p[j] == '*':
            j += 1
        return j == n

# @lc code=end

