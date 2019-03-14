# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.Power(base, abs(exponent) >> 1)
        result *= result
        if (abs(exponent) & 1 == 1):
            result = base * result
        if exponent >= 0:
            return result
        else:
            return 1/result