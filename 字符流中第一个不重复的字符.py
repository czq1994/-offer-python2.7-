# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.s = ''

    def FirstAppearingOnce(self):
        # write code here
        if not self.s:
            return '#'
        for key in self.s:
            if self.dic[key] == 1:
                return key
        return '#'

    def Insert(self, char):
        # write code here
        if char not in self.dic:
            self.dic[char] = 1
            self.s += char  # 只有当char第一次出现时，s才会更新，这样s的长度固定
        else:
            self.dic[char] += 1