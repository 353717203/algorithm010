#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        dot = []    # 记录每个未填写数字的坐标
        row = [set(range(1, 10)) for _ in range(9)]     # 记录每一行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]     # 记录每一列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]   # 记录每个9*9方格可用数字
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    dot.append((i, j))
                else:
                    num = int(board[i][j])
                    # 删除对应行、列、块已使用数字
                    row[i].remove(num)
                    col[j].remove(num)
                    block[(i // 3) * 3 + j // 3].remove(num)

        self.dfs(board, row, col, block, dot, 0) 

    def dfs(self, board, row, col, block, dot, step):
        if step == len(dot):    # 遍历完所有未填写数字的坐标
            return True

        i, j = dot[step]
        k = (i // 3) * 3 + j // 3
        union = row[i] & col[j] & block[k]      # 求交集，获取行、列、块都可用的数字

        for num in union:
            board[i][j] = str(num)
            row[i].remove(num)
            col[j].remove(num)
            block[k].remove(num)

            if self.dfs(board, row, col, block, dot, step + 1):
                return True

            board[i][j] = '.'
            row[i].add(num)
            col[j].add(num)
            block[k].add(num)
        return False

# @lc code=end

