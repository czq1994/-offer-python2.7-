# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        s = self.reverseWord(s)  # 整个翻转

        ls = s.split(' ')
        res = ''
        for ss in ls:
            res += (self.reverseWord(ss) + ' ')
        return res[:-1]

    def reverseWord(self, s):
        ls = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
        res = ''
        for i in range(len(s)):
            res += ls[i]
        return res