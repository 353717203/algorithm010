#
# app=leetcode.cn id=40 lang=python
#
# [面试40] 最小的K个数
#
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        res = self.quickSearch(arr, 0, len(arr) - 1, k - 1)
        return res
        
    # Solution_1 —— 排序
    def sortk(self, arr, k):
        arr.sort()
        return arr[:k]

    # Solution_2 —— 堆（大根堆）
    def heap_max(self, arr, k):
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for n in arr[k:]:
            if -hp[0] > n:
                heapq.heappop(hp)
                heapq.heappush(hp, -n)
        res = [-x for x in hp]
        return res

    # Solution_3 —— 快排
    def partition(self, arr, l, r):
        v = arr[l]
        i, j = l, r
        while True:
            while i < j and arr[j] >= v:
                j -= 1
            while i < j and arr[i] <= v:
                i += 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[l] = arr[j]
        arr[j] = v
        return j

    def quickSearch(self, arr, l, r, k):
        j = self.partition(arr, l, r)
        if j == k:
            return arr[:k+1]
        elif j > k:
            return self.quickSearch(arr, l, j - 1, k)
        else:
            return self.quickSearch(arr, j + 1, r, k)

# code=start