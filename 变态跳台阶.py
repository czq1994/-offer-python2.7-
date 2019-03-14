# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        return 2**(number-1)