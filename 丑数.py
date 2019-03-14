# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        ugly = [1]  # 第一个丑数
        m2 = 0  # 记录已有丑数中乘2后能大于已有丑数的最大值的数的下标
        m3 = 0  # 乘3
        m5 = 0  # 乘5
        i = 1
        while i < index:  # 从第二个丑数开始进入循环
            minVal = min(ugly[m2] * 2, ugly[m3] * 3, ugly[m5] * 5)
            ugly.append(minVal)
            while ugly[m2] * 2 <= minVal:
                m2 += 1
            while ugly[m3] * 3 <= minVal:
                m3 += 1
            while ugly[m5] * 5 <= minVal:
                m5 += 1
            i += 1
        return ugly[-1]
