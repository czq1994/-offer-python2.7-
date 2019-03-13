# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows, cols = len(array), len(array[0])
        i = 0
        j = cols-1
        while i < rows and j >= 0:
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
        return False