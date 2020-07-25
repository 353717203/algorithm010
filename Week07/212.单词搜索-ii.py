#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 构建字典树
        trie = {}
        for word in words:
            nodes = trie
            for c in word:
                if c not in nodes:
                    nodes[c] = {}
                nodes = nodes[c]
            nodes['#'] = word   # 字典树结束符

        m, n = len(board), len(board[0])
        
        res = []
        def dfs(trie, x, y):
            c = board[x][y]
            if c not in trie:
                return 
            curr = trie[c]
            word_match = curr.pop('#', False)
            if word_match:
                res.append(word_match)

            board[x][y] = '*'
            for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                dx, dy = x + i, y + j
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] != '*' and board[dx][dy] in curr:
                    dfs(curr, dx, dy)
            board[x][y] = c

            # 优化剪纸：删除已经匹配的节点
            if not curr:
                trie.pop(c)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(trie, i, j)

        return res        
        
# @lc code=end

