#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # Solution_1 —— DFS
        def dfs(root, ans):
            if not root:
                ans.append('*')
            else:
                ans.append(str(root.val))
                dfs(root.left, ans)
                dfs(root.right, ans)

        # Solution_2 —— BFS
        def bfs(root, ans):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                ans.append(str(node.val) if node else '*')
                if node:
                    queue.extend([node.left, node.right])

        res = []
        # dfs(root, res)
        bfs(root, res)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # Solution_1 —— DFS
        def dfs(nums):
            n = next(nums)
            if n == '*':
                return None
            node = TreeNode(int(n))
            node.left = dfs(nums)
            node.right = dfs(nums)
            return node

        # Solution_2 —— BFS
        def bfs(nums):
            if not nums:
                return 
            nodes = [(TreeNode(int(v)) if v != '*' else None) for v in nums.split(',')]
            i, j = 0, 1
            while j < len(nodes):
                if nodes[j] is not None:
                    nodes[i].left = nodes[j]
                    j += 1
                    nodes[i].right = nodes[j]
                    j += 1
                i += 1
            return nodes[0]

        # return dfs(iter(data.split(",")))
        return bfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

