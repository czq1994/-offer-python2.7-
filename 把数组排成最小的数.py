# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        #cmp = lambda n1, n2:
        numbers = [str(val) for val in numbers]
        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                # 由于字符串长度相等，因此直接比较字符串的大小和比较数字大小是等价的
                return 1
            elif num1 + num2 < num2 + num1:
                    return -1
            else:
                return 0
        x = lambda n1,n2:int(n1+n2)-int(n2+n1)# 指定比较方式
        #res = sorted(numbers, cmp = compare)  # compare与x皆可
        res = sorted(numbers, cmp = x)
        res = ''.join(res)
        return res
