# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here 其实就是斐波那契数列
        if number < 1:
            return 0
        if number == 1 or number == 2:
            return number

        cur1, cur2 = 1, 2
        for i in range(3, number + 1):
            a = cur2
            cur2 = cur1 + cur2
            cur1 = a
        return cur2
