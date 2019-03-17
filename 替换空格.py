# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
     def replaceSpace(self,s):
        # write code here
        length = len(s)
        for i in s:
            if i == ' ':
                s += '  '  #新的长度
        new_length = len(s)
        s = list(s)
        print(length,new_length)
        i, j = length-1, new_length-1
        while i != j:
            if s[i] == ' ':
                j = j-2
                s[j:j+3] = '%20'
            else:
                s[j] = s[i]
            j -= 1
            i -= 1
        return ''.join(s)
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.split(' ')
        return '%20'.join(s)
'''
