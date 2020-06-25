#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root)

    # Solution_1 —— 递归
    def dfs(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.dfs(root.left)
        self.dfs(root.right)
        return root
# @lc code=end

