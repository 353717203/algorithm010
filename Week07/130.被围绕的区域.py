#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        return self.helpDFS(board)
        # return self.helpBFS(board)
        

    # Solution_1 —— DFS
    # 通过DFS找到边界上的'O'以及连通的'O'标记为'*'，然后将剩下的'O'转换为'X', 最后将'*'转换为'O'
    def helpDFS(self, board):
        if not board:
            return []

        m, n = len(board), len(board[0])
        # 将所有和边界上'O'相邻的标记为'*'
        for i in range(m):
            if board[i][0] == 'O' : self.dfs(board, m, n, i, 0, '*')
            if board[i][n - 1] == 'O': self.dfs(board, m, n, i, n - 1, '*')

        for j in range(n):
            if board[0][j] == 'O': self.dfs(board, m, n, 0, j, '*')
            if board[m - 1][j] == 'O': self.dfs(board, m, n, m - 1, j, '*')

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
        return board

    def dfs(self, board, m, n, x, y, c):
        board[x][y] = c
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = x + i, y + j
            if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'O':
                self.dfs(board, m, n, dx, dy, c)

    # Solution_2 —— BFS
    def helpBFS(self, board):
        if not board:
            return []

        m, n = len(board), len(board[0])
        # 将所有和边界上'O'相邻的标记为'*'
        for i in range(m):
            if board[i][0] == 'O' : self.bfs(board, m, n, i, 0, '*')
            if board[i][n - 1] == 'O': self.bfs(board, m, n, i, n - 1, '*')

        for j in range(n):
            if board[0][j] == 'O': self.bfs(board, m, n, 0, j, '*')
            if board[m - 1][j] == 'O': self.bfs(board, m, n, m - 1, j, '*')

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
        return board

    def bfs(self, board, m, n, row, col, c):
        board[row][col] = c
        queue = [(row, col)]
        while queue:
            x, y = queue.pop(0)
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx, dy = x + i, y + j
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'O':
                    board[dx][dy] = c
                    queue.append((dx, dy))

    # Solution_3 —— 并查集
    def unionFind(self, board):
        m, n = len(board), len(board[0])
        dummy = m * n
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        self.union(i * n + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            dx, dy = x + i, y + j
                            if board[dx][dy] == 'O':
                                self.union(i * n + j, (i + x) * n + (j + y))

        for i in range(m):
            for j in range(n):
                if find(dummy) == find(i * n + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def union(self, arr, i, j):
        p = self.find(arr, i)
        q = self.find(arr, j)
        arr[p] = q

    def find(self, arr, i):
        root = i
        while arr[root] != root:
            root = arr[root]
        while arr[i] != i:
            x = i; i = arr[i]; arr[x] = root
        return root
# @lc code=end

