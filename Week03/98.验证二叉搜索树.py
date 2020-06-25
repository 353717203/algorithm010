#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursive(root, float('-inf'), float('inf'))
        # return self.midTraversal(root)

    # Solution_1 —— 递归
    def recursive(self, root, low, up):
        if not root:
            return True
        if not low < root.val < up:
            return False
        return self.recursive(root.left, low, root.val) \
            and self.recursive(root.right, root.val, up)
        # if not self.recursive(root.left, low, root.val):
        #     return False
        # if not self.recursive(root.right, root.val, up):
        #     return False
        # return True

    # Solution_2 —— 中序遍历
    def midTraversal(self, root):
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
# @lc code=end

