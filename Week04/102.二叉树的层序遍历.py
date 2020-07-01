#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        # self.dfs(0, root, res)
        self.bfs(root, res)
        return res

    # Solution_1 —— DFS
    def dfs(self, depth, root, res):
        if not root:
            return 
        if len(res) == depth:
            res.append([])
        res[depth].append(root.val)
        if root.left:
            self.dfs(depth + 1, root.left, res)
        if root.right:
            self.dfs(depth + 1, root.right, res)

    # Solution_2 —— BFS
    def bfs(self, root, res):
        if not root:
            return 
        queue = [root]
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)

# @lc code=end

