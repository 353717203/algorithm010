#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        index = {element: i for i, element in enumerate(inorder)}
        return self.dfs(preorder, inorder, index, 0, len(preorder) - 1, 0, len(inorder) - 1)

    # Solution_1 —— 递归
    
    def dfs(self, preorder, inorder, index, pre_l, pre_r, ino_l, ino_r):
        if pre_l > pre_r:
            return None
        # 前序遍历第一个元素为根节点，哈希表中找到根节点在中序遍历的位置
        pre_root = pre_l
        i = index[preorder[pre_root]]
        root = TreeNode(preorder[pre_root])
        # 左子树节点数目
        size_left = i - ino_l

        # 前序：[左边界 + 1 : 左边界 + 左子树节点数], 中序：[左边界 : 根节点索引 - 1]
        root.left = self.dfs(preorder, inorder, index, pre_l + 1, pre_l + size_left, ino_l, i - 1)

        # 前序：[左边界 + 左子树节点数 + 1 : 右边界], 中序：[根节点索引 + 1 : 右边界]
        root.right = self.dfs(preorder, inorder, index, pre_l + size_left+ 1 , pre_r, i + 1, ino_r)
        return root
# @lc code=end

