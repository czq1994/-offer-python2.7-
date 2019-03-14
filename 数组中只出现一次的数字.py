# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 2:
            return []
        length = len(array)
        res1 = 0
        res2 = 0
        digit = self.find_dif_digit(array)
        for i in range(length):
            if (array[i] >> digit) & 1 == 1:
                res1 ^= array[i]
            elif (array[i] >> digit) & 1 == 0:
                res2 ^= array[i]
        return [res1, res2]

    def find_dif_digit(self, array):
        # 找到数组中不同的两个数，其二进制从右边起第几位开始不同
        # 数组中所有元素的异或结果等于两个只出现一次的数的异或结果
        res = 0
        for i in range(len(array)):
            res ^= array[i]
        digit = 0
        while res:
            if res & 1 == 0:
                res = res >> 1
                digit += 1
            else:
                break
        return digit