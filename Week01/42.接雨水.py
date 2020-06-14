#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def Dynamic(self, height, size):
        # Solution_动态
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        # 遍历左端最高
        for i in range(1, size):
            if height[i] > left_max[i - 1]:
                left_max[i] = height[i]
            else:
                left_max[i] = left_max[i - 1]

        # 遍历右端最高
        for i in range(size - 2, -1, -1):
            if height[i] > right_max[i + 1]:
                right_max[i] = height[i]
            else:
                right_max[i] = right_max[i + 1]

        # 计算积水
        ans = 0
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans
    
    def Dequeue(self, height, size):
        # Solution_双指针
        left_max, right_max = 0, 0
        l, r, ans = 0, size - 1, 0

        while l <= r:
            if left_max < right_max:
                # 从左往右处理，left_max可信，left_max < right_max时，无论right_max是否出现更大，都不产生影响
                ans += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
                l += 1
            else:
                # 从右往左处理，right_max可信，left_max >= right_max时，无论left_max是否出现更大，都不产生影响
                ans += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
                r -= 1
                
        return ans

    def Stack(self, height, size):
        # Solution_单调栈
        stack = []
        ans, index = 0, 0
        while index < size:
            while len(stack) != 0 and height[index] > height[stack[-1]]:
                w = stack[-1]
                stack.pop()
                if len(stack) == 0:
                    break
                bounded_height = min(height[index], height[stack[-1]]) - height[w]
                ans += bounded_height * (index - stack[-1] - 1)

            stack.append(index)
            index += 1
        return ans

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size == 0:
            return 0
        
        # return self.Dynamic(height, size)
        # return self.Dequeue(height, size)
        return self.Stack(height, size)
    
# @lc code=end

