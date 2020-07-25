#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        # res = []
        # self.dfs(start, end, bank, 0, res)
        # return -1 if not res else min(res)
        # return self.bfs(start, end, bank)
        return self.debfs(start, end, bank)

    change = {"A": "CGT", "C": "AGT", "G": "CAT", "T": "CGA"}

    # Solution_1 —— DFS + 回溯
    def dfs(self, start, end, bank, step, res):
        if start == end: 
            res.append(step)
        if not bank: return 
        for i, s in enumerate(start):
            for c in Solution.change[s]:
                new = start[:i] + c + start[i + 1:]
                if new in bank:
                    bank.remove(new)
                    self.dfs(new, end, bank, step + 1, res)
                    bank.append(new)

    # Solution_2 —— BFS
    def bfs(self, start, end, bank):
        queue = []
        queue.append((start, 0))
        while queue:
            curr, step = queue.pop(0)
            if curr == end:
                return step
            for i, s in enumerate(curr):
                for c in Solution.change[s]:
                    new = curr[:i] + c + curr[i+1:]
                    if new in bank:
                        bank.remove(new)
                        queue.append((new, step + 1))
        return -1

    # Solution_3 —— 双向BFS
    # 分别从start和end开始扩散，每次扩散长度小的(分枝小的)，如果相遇了则找到变化次数
    def debfs(self, start, end, bank):
        left, right = {start}, {end}
        step = 0
        while left:
            step += 1
            # 存储中间基因
            mid = set()
            for word in left:
                for i, s in enumerate(word):
                    for c in Solution.change[s]:
                        new = word[:i] + c + word[i+1:]
                        # 左右扩散相遇
                        if new in right:
                            return step
                        if new in bank:
                            mid.add(new)
                            bank.remove(new)
            # 分枝放入队列（叶子节点入队）
            left = mid
            # 从分枝较小的一端扩散（叶子节点少的开始扩散）
            if len(left) > len(right):
                left, right = right, left

        return -1
# @lc code=end

