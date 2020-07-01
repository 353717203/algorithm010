#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        wordList = set(wordList)
        # return self.bfs(beginWord, endWord, wordList)
        # return self.bfs_alph(beginWord, endWord, wordList)
        return self.debfs(beginWord, endWord, wordList)
        
    # Solution_1 —— BFS(转换列表)
    def bfs(self, beginWord, endWord, wordList):
        # 建立可转换列表
        changes = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + '*' + word[i + 1:]
                changes[s].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord:True}
        while queue:
            curr, step = queue.pop(0)
            for i in range(len(beginWord)):
                new = curr[:i] + '*' + curr[i+1:]
                for k in changes[new]:
                    if k == endWord:
                        return step + 1
                    if k not in visited:
                        visited[k] = True
                        queue.append((k, step + 1))
        return 0

    # Solution_2 —— BFS(遍历可转换字母)
    def bfs_alph(self, beginWord, endWord, wordList):
        queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)
        alph_list = list('abcdefghijklmnopqrstuvwxyz')
        while queue:
            curr, step = queue.pop(0)
            for i in range(len(curr)):
                for c in alph_list:
                    new = curr[:i] + c + curr[i+1:]
                    if new in wordList:
                        if new == endWord:
                            return step + 1
                        if new not in visited:
                            queue.append((new, step + 1))
                            visited.add(new)
        return 0

    # Solution_3 —— 双向BFS
    def debfs(self, beginWord, endWord, wordList):
        left, right = [beginWord], [endWord]
        alph_list = list('abcdefghijklmnopqrstuvwxyz')
        step = 1
        while left:
            mid = set()
            for word in left:
                for i in range(len(beginWord)):
                    for c in alph_list:
                        new = word[:i] + c + word[i+1:]
                        if new in right:
                            return step + 1
                        if new in wordList:
                            mid.add(new)
                            wordList.remove(new)
            left = mid
            step += 1
            if len(left) > len(right):
                left, right = right, left
        return 0

# @lc code=end

