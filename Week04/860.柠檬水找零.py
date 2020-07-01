#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five , ten = 0, 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
        
# @lc code=end

