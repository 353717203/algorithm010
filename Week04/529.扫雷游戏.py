#
# @lc app=leetcode.cn id=529 lang=python
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        row, col = len(board), len(board[0])
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        # self.dfs(board, x, y, row, col)
        # -------------------------------
        self.bfs(board, x, y, row, col)
        return board

    def mine_nums(self, x, y, row, col, board):
        num = 0
        # 计算(x, y)坐标8个方向上地雷数量
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if i == 0 and j == 0: continue
                dx, dy = x + i, y + j
                if 0 <= dx < row and 0 <= dy < col and board[dx][dy] == 'M':
                    num += 1
        return num

    # Solution_1 —— DFS
    def dfs(self, board, x, y, row, col):
        num = self.mine_nums(x, y, row, col, board)
        if num > 0:
            board[x][y] = str(num)
            return 
        board[x][y] = 'B'
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if i == 0 and j == 0: continue
                dx, dy = x + i, y + j
                if 0 <= dx < row and 0 <= dy < col and board[dx][dy] == 'E':
                    self.dfs(board, x + i, y + j, row, col)

    # Solution_2 —— BFS
    def bfs(self, board, x, y, row, col):
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            num = self.mine_nums(x, y, row, col, board)
            if num > 0:
                board[x][y] = str(num)
                continue
            board[x][y] = 'B'
            for i in [1, 0, -1]:
                for j in [1, 0, -1]:
                    if i == 0 and j == 0: continue
                    dx, dy = x + i, y + j
                    if 0 <= dx < row and 0 <= dy < col and board[dx][dy] == 'E':
                        queue.append((dx, dy))
                        board[dx][dy] = 'B'

# @lc code=end

