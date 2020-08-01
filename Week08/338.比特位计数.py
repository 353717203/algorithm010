#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        # return self.helpBit(num)
        # ------------------------
        return self.helpBits(num)
     
    # Soulution_1 —— 位运算
    # n >> 1去掉二进制最后一位，且n >> 1在之前已经进行过计算
    # 当最低位是0，n与n >> 1的1数目相同，当最低位为1，n的数目为n >> 1的数目加1
    def helpBit(self, num):
        dp = [0] * (num + 1)
        for n in range(0, num + 1):
            dp[n] = dp[n >> 1] + (n & 1)
        return dp

    # Solution_2 —— 位运算
    # 如果n为偶数，则dp[n]与dp[n/2]相同，因为n/2实质是二进制右移一位，1的数量不变
    # 如果n为奇数，则dp[n]=dp[n-1]+1，n为基数那么n - 1为偶数，偶数的低位为0，所以奇数比他上一个偶数多1
    def helpBits(self, num):
        dp = [0] * (num + 1)
        for n in range(1, num + 1):
            if n % 2 == 0:
                dp[n] = dp[n >> 1]
            else:
                dp[n] = dp[n - 1] + 1
        return dp
# @lc code=end

