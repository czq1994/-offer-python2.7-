# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        count = 0
        res = 0
        mark = 1
        if s[0] in '+-':  # 第一位的正负
            if s[0] == '+':
                mark = 1
            else:
                mark = -1
            s = s[1:]
        if s == '':
            return 0
        # 其他位只能出现数字，且第一位不能出现0
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in '0123456789':
                return 0
            elif s[i] == '0' and i == 0:
                return 0
            res += int(s[i]) * (10 ** count)
            count += 1
        return mark * res
