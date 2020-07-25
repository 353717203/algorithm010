#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValid(board)

    # Solution_1
    def isValid(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                k = (i // 3) * 3 + j // 3
                if num in row[i] or num in col[j] or num in block[k]:
                    return False
                row[i].add(num)
                col[j].add(num)
                block[k].add(num)
        return True

    # Solution_2
    # i, j分别为行号和列号，仅当同一行i、同一列j或者同一块有相同的元组时，数独不合法
    # (i, num)元组存入的是(1, '3')，不会和(num, j)的('1', 3)重复
    def isValidSD(self, board):
        stack = []
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    stack += [(i, num), (num, j), (i / 3, j / 3, num)]
        return len(stack) == len(set(stack))
# @lc code=end

