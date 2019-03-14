# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n <= 0 or not s:
            return s
        length = len(s)
        if n >= length:
            n = n % length
            if n == 0:  # 整数倍相当于没有旋转
                return s
        s = self.reverseWord(s)
        s1 = self.reverseWord(s[:-n])  # 分别对两部分进行翻转
        s2 = self.reverseWord(s[-n:])
        res = s1 + s2  # 合在一起再进行翻转
        return res

    def reverseWord(self, word):
        ls = list(word)
        i = 0
        j = len(ls) - 1
        while i < j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
        s = ''
        for i in range(len(ls)):
            s += ls[i]
        return s
