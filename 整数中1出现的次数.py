# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n:
            return 0
        count = 0
        s = str(n)
        length = len(s)
        if length < 2:
            if int(s[0]) >= 1:
                return 1
            else:
                return 0
        # 2325拆成1到325和326到2325两部分
        high = int(s[0])
        other = int(s[1:])
        # 326到2325之间1在最高位出现的次数
        if high > 1:
            count += 10 ** (length - 1)
        elif high == 1:
            count += other + 1
        # 326到2325之间1在其余位上出现的次数
        count += high * (length - 1) * 10 ** (length - 2)

        return count + self.NumberOf1Between1AndN_Solution(other)
