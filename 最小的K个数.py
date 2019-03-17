# -*- coding:utf-8 -*-
# 1. 堆排序方法
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        length = len(tinput)
        ls = []
        if k == length:
            return sorted(tinput)
        if k > length or k < 1 or length <= 0:
            return []
        for i in range(length):

            if i < k:
                ls.append(tinput[i])
                if i == k - 1:  # 此时正好k个元素，开始初始化最大堆
                    start = (0 + i) // 2
                    for j in range(start, -1, -1):
                        print(j)
                        self.heap_once(ls, j, k - 1)
                        print(ls)
            else:
                if tinput[i] < ls[0]:
                    ls[0] = tinput[i]
                    self.heap_once(ls, 0, k - 1)
                else:
                    pass
        return sorted(ls)

    def heap_once(self, ls, start, end):
        i = start
        save = ls[start]
        j = i * 2 + 1
        while j <= end:
            print(j)
            if j + 1 <= end and ls[j + 1] > ls[j]:
                j += 1
            if ls[i] < ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
                i = j
                j = 2 * j + 1
            else:
                break
        # ls[i] = save
        
# 2. 类似快排的方法，时间复杂度O(n)
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k == len(tinput):
            return sorted(tinput)
        left = 0
        right = len(tinput) - 1
        while left <= right:
            index = self.partition(tinput, left, right)
            if index == k:
                return sorted(tinput[:k])
            elif index > k:
                right = index-1
            else:
                left = index+1
        return []
        
    def partition(self, nums, i, j):
        base = nums[i]
        while i < j:
            while nums[j] >= base and i < j:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while nums[i] <= base and i < j:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = base
        return i
