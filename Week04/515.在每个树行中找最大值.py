#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # nums = {}
        # self.dfs(root, 0, nums)
        # return [c for c in nums.values()]
        # ---------------------------------
        return self.bfs(root)
        
    # Solution_1 —— DFS
    def dfs(self, root, index, maps):
        if not root:
            return []
        if index not in maps:
            maps[index] = root.val
        else:
            maps[index] = max(root.val, maps[index])
        if root.left:
            self.dfs(root.left, index + 1, maps)
        if root.right:
            self.dfs(root.right, index + 1, maps)

    # Solution_2 —— BFS
    def bfs(self, root):
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            max_num = float('-inf')
            for _ in range(len(queue)):
                node = queue.pop(0)
                max_num = max(node.val, max_num)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_num)
        return res
        
# @lc code=end

