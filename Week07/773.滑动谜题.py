#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        return self.helpBFS(board)
    
    # Solution_1 —— BFS
    def helpBFS(self, board):
        board = board[0] + board[1]
        print(board)
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        queue = [(tuple(board), board.index(0), 0)]
        visited = set()
        while queue:
            path, zero, step = queue.pop(0)
            if path == (1, 2, 3, 4, 5, 0):
                return step
            for index in list(moves[zero]):
                l_path = list(path)
                # 0的位置和相邻的位置进行交换
                l_path[zero], l_path[index] = l_path[index], l_path[zero]
                l_path = tuple(l_path)
                if l_path not in visited:
                    queue.append((l_path, index, step + 1))
            visited.add(path)
        return -1
            
# @lc code=end

