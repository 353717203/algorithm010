#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        return self.help(str)

    def help(self, str):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        str = str.lstrip()
        lens = len(str)
        
        if lens == 0:
            return 0
        
        i = 0
        num = 1
        if str[i] == '+':
            num = 1
            i = i + 1
        elif str[i] == '-':
            num = -1
            i = i + 1
        
        ans = 0
        while i < lens and str[i].isdigit():
            ans = int(str[i]) + ans * 10
            if ans > INT_MAX:
                if num == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i = i + 1
        return ans*num
            
# @lc code=end

