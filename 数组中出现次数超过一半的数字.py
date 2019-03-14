# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 0
        for i in range(len(numbers)):
            if count == 0:
                target = numbers[i]
                count = 1
            elif numbers[i] == target:
                count += 1
            elif numbers[i] != target:
                count -= 1
        if count > 0 and self.isMoreHalf(numbers, target):
            return target
        else:
            return 0

    def isMoreHalf(self, numbers, target):
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == target:
                count += 1
        if count > len(numbers) // 2:
            return True
        else:
            return False
