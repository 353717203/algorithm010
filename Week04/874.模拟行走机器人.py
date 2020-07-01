#
# @lc app=leetcode.cn id=874 lang=python
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        return self.robot(commands, obstacles)
        
    # Solution_1 —— 模拟
    def robot(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacles_set = set(map(tuple, obstacles))
        x, y, temp, res = 0, 0, 0, 0
        for n in commands:
            if n == -2: temp = (temp - 1) % 4
            elif n == -1: temp = (temp + 1) % 4
            else:
                for _ in range(n):
                    if (x + dx[temp], y + dy[temp]) not in obstacles_set:
                        x += dx[temp]
                        y += dy[temp]
                        res = max(res, x * x + y * y)
        return res
# @lc code=end

