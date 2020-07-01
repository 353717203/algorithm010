#
# @lc app=leetcode.cn id=126 lang=python
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        res = self.bfs(beginWord, endWord, wordList)
        return res

    def bfs(self, beginWord, endWord, wordList):
        # 建立转换列表
        changes = defaultdict(list)
        for s in wordList:
            for i in range(len(s)):
                new = s[:i] + '*' + s[i+1:]
                changes[new].append(s)
        # 记录节点和访问路径
        queue, nextq = [(beginWord, [beginWord])], []
        visited, res = set(), []
        while queue:
            # 遍历当前层节点，相邻下一层节点不入队
            while queue:
                curr, path = queue.pop(0)
                if curr == endWord:
                    res.append(path)
                visited.add(curr)
                for i in range(len(curr)):
                    new = curr[:i] + "*" + curr[i+1:]
                    for word in changes[new]:
                        if word not in visited:
                            # 节点未被访问，加入下一层队列并添加路径
                            nextq.append((word, path + [word]))
            if res:
                return res
            # 完成当前层遍历，遍历下一层所有节点
            queue, nextq = nextq, queue
        return []
# @lc code=end

