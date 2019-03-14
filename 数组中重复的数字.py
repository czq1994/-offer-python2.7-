# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        for i in range(length):
            while i != numbers[i]:
                val = numbers[i]
                if numbers[val] == val:
                    duplication[0] = val
                    return True
                else:
                    numbers[i], numbers[val] = numbers[val], numbers[i]
        return False
