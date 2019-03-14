# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n < 2:
            return n
        small = 0
        big = 1
        i = 2
        while i <= n:
            small_save = small
            small = big
            big = small_save + big
            i += 1
        return big