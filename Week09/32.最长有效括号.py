#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return self.helpStack(s)
        # ------------------------
        return self.helpCount(s)

    # Solution_1 —— 栈
    # 使用栈来记录括号的下标，栈底元素始终保持一个未被匹配的')'下标，遇到'('将下标入栈，遇到')'出栈
    # 如果当前栈为空，说明当前')'没有匹配的'('，入栈当前')'下标，不为空则当前下标减去栈顶元素
    # 如果一开始栈为空，开始将'('下标入栈，不满足入保存')'下标，因此开始在栈中初始化下标为-1
    def helpStack(self, s):
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
                continue
            stack.pop()
            # 栈为空，当前')'前面已经没有左括号，更新起点下标
            if not stack:
                stack.append(i)
            else:
                res = max(res, i - stack[- 1])
        return res

    # Solution_2 —— 正逆向遍历
    # 使用两个计数器left，right来统计遇到的左右括号，每当左右括号相等时，计算有效括号的长度
    # 左->右遍历：当right > left时，当前右括号无效，清空left,right
    # 右->左遍历：当left > right时，当前左括号无效，清空left,right
    def helpCount(self, s):
        left = right = res = 0
        for c in s:
            if c == '(': 
                left += 1 
            else: 
                right += 1
            if left == right:
                res = max(res, 2 * left)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(': 
                left += 1 
            else: 
                right += 1
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0
        return res

# @lc code=end

