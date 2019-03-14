# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) != 5:
            return False
        numbers.sort()  # 排序
        blank_times = 0
        zero_times = numbers.count(0)  # 0出现的次数
        length = len(numbers)

        for i in range(zero_times, length - 1):
            if numbers[i] + 1 != numbers[i + 1]:
                if numbers[i + 1] == numbers[i]:  # 如果存在相邻两个相等的情况，没救
                    return False
                blank_times += numbers[i + 1] - numbers[i] - 1
        if blank_times <= zero_times:
            return True
        else:
            return False
