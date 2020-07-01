#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        return self.binaryAll(matrix, target)
        # return self.binaryResearch(matrix, target)

    # Solution_1 —— 二分（映射一维）
    def binaryAll(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid / col][mid % col] < target:
                l = mid + 1
            elif matrix[mid / col][mid % col] > target:
                r = mid - 1
            else:
                return True
        return False

    # Solution_2 —— 二分（分别查找行和列）
    def binaryResearch(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        # 二分查找行
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid][m - 1] < target:
                l = mid + 1
            else:
                r = mid
        # 目标值所在行
        x = l
        # 二分查找列
        l, r = 0, m - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[x][mid] < target:
                l = mid + 1
            else:
                r = mid
        # 目标值所在列
        y = l
        return matrix[x][y] == target
# @lc code=end

