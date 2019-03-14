# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 0
            dic[s[i]] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1