# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        low = 1
        high = 2
        for i in range(2, number):
            low_save = low
            low = high
            high = low_save + high
        return high