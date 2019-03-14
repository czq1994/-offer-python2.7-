# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        cur = ''
        self.helper(ss,res,cur)
        return sorted(list(set(res)))
    def helper(self,ss,res,cur):
        if not ss:
            res.append(cur)
        for i in range(len(ss)):
            self.helper(ss[:i] + ss[i+1:], res, cur+ss[i])
        return res