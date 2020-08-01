#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return self.moveBin(n)
        # ----------------------
        # return self.helpBin(n)
        return bin(n).count('1')

    # Solution_1 —— 位移动
    # 每次向右移动一位二进制位，判断最后一位是否为1，需要移动32次
    def moveBin(self, n):
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    # Solution_2 —— 位运算
    # n & (n - 1)会删除最后一位1，因此只需要移动1的个数次
    def helpBin(self, n):
        res = 0
        while n:
            res += 1
            n = n & (n - 1)
        return res
# @lc code=end

