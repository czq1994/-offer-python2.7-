# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 1:
            return []
        res = []
        cur = [1]
        count = 1
        i = 2
        while cur[0] <= tsum//2:
            if count < tsum:
                cur.append(i)
                count += i
                i += 1
            elif count > tsum:
                val = cur.pop(0)
                count -= val
            else:
                res.append(cur[:])
                cur.append(i)
                count += i
                i += 1
        return res

'''
  def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        if tsum < 3:
            return []
        start = 1
        end = 2
        mid = tsum // 2
        ls = [start, end]
        while start <= mid:
            curSum = sum(ls)
            if curSum == tsum:
                res.append(ls[:])  #这里对ls加了个冒号是复制的意思，防止下面的操作篡改ls
                end += 1
                ls.append(end)
            elif curSum < tsum:
                end += 1
                ls.append(end)
            else:
                start += 1
                ls.pop(0)
        return res
'''