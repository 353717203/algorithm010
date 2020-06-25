#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root, p, q)
    
    # Solution_1 —— DFS + 后续遍历
    def dfs(self, root, p, q):
        if not root or root == q or root == p:
            return root
        # 遍历左右子树
        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p, q)
        
        if not l and not r: return 
        # p, q 同在root右侧
        if not l: return r
        # p, q 同在root左侧
        if not r: return l
        # p, q 在root的异侧
        return root
# @lc code=end

