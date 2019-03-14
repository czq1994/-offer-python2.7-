# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        global count
        count = 0
        self.inverseP(data)
        return count % 1000000007

    def inverseP(self, data):
        global count
        length = len(data)
        if length <= 1:
            return data
        mid = length // 2
        left = self.inverseP(data[:mid])
        right = self.inverseP(data[mid:])
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                count += len(left) - i   # 唯一和归并排序不一样的地方
                j += 1
        if i < len(left):
            result += left[i:]
        elif j < len(right):
            result += right[j:]
        return result
