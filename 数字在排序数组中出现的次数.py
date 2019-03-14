# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 用二分法分别找到第一个k和最后一个k
        if not data:
            return 0
        start = 0
        end = len(data) - 1
        first_index = self.find_first(data, k, start, end)
        last_index = self.find_last(data, k, start, end)
        if first_index == -1 or last_index == -1:
            return 0
        return last_index - first_index + 1

    def find_first(self, data, k, start, end):
        mid = (start + end) // 2
        if start > end:
            return -1
        if data[mid] == k:
            # mid为表头或者mid左边的元素仍然等于k
            if mid - 1 < start or data[mid - 1] < k:
                return mid
            elif data[mid - 1] == k:
                return self.find_first(data, k, start, mid - 1)
        if data[mid] > k:
            return self.find_first(data, k, start, mid - 1)
        if data[mid] < k:
            return self.find_first(data, k, mid + 1, end)

    def find_last(self, data, k, start, end):
        mid = (start + end) // 2
        if start > end:
            return -1
        if data[mid] == k:
            if mid + 1 > end or data[mid + 1] > k:
                return mid
            elif data[mid + 1] == k:
                return self.find_last(data, k, mid + 1, end)
        if data[mid] > k:
            return self.find_last(data, k, start, mid - 1)
        if data[mid] < k:
            return self.find_last(data, k, mid + 1, end)