#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # return self.countOne(n)
        # ------------------------
        return self.helpBit(n)

    # Solution_1 —— 统计二进制中1的个数
    # 2的幂次方的整数二进制位有且仅有一个1
    def countOne(self, n):
        res = 0
        while n:
            res += n & 1
            if res >= 2:
                return False
            n >>= 1
        return True

    # Solution_2 —— 与运算
    # 因为2的幂次方的整数二进制位有且仅有一个1，所以(n - 1) & n = 0
    def helpBit(self, n):
        return n & (n - 1) == 0
# @lc code=end

