#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        res = self.bfs(root)
        # self.dfs(root, res, 0)
        return res
    
    # Solution_1 —— DFS遍历
    def dfs(self, root, res, dep):
        if root:
            if len(res) <= dep:
                res.append([])
            res[dep].append(root.val)
            for c in root.children:
                self.dfs(c, res, dep + 1)

    # Solution_2 —— BFS遍历
    def bfs(self, root):
        queue, res = [root], []
        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return res
        
# @lc code=end

