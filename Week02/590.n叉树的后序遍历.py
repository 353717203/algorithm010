#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N叉树的后序遍历
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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Solution_1 —— 递归实现遍历
        # ---------------------------
        if not root:
            return []

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            for c in root.children:
                self.dfs(c, res)
        res.append(root.val)
# @lc code=end

