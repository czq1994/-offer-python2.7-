# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here 补码：除符号位，按位取反，最后末尾加1
        from ctypes import *
        count = 0
        while c_int(n).value:
            count += 1
            n = (n - 1) & n
        return count
