#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        nums = [-1] * n
        # nQueues = [['.'] * n for _ in range(n)]
        # self.backtrack(nQueues, nums, 0, res)
        self.dfs(nums, 0, [], res)
        return res

    # Solution_1 —— 回溯
    def backtrack(self, arr, nums, row, ans):
        # 到达边界
        if row == len(arr):
            # 二维变一维添加到res中
            tmp_list = [] 
            for c in arr:
                tmp = ''.join(c)
                tmp_list.append(tmp)
            ans.append(tmp_list)
            return 

        # 遍历所有列
        for col in range(len(arr)):
            nums[row] = col
            # 符号皇后放置条件
            if self.isValid(nums, row):
                arr[row][col] = 'Q'
                self.backtrack(arr, nums, row + 1, ans)
                arr[row][col] = '.'

    # Solution_2 —— DFS
    def dfs(self, nums, row, path, ans):
        if row == len(nums):
            ans.append(path)
            return 
        for col in range(len(nums)):
            nums[row] = col
            if self.isValid(nums, row):
                tmp = '.' * len(nums)
                s = [tmp[ :col] + 'Q' + tmp[col + 1: ]]
                self.dfs(nums, row + 1, path + s, ans)

    def isValid(self, nums, x):
        for i in range(x):
            if nums[i] == nums[x] or abs(nums[i] - nums[x]) == abs(i - x):
                return False
        return True
# @lc code=end

