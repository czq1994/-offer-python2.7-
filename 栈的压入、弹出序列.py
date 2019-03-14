# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here

        fuzhu = []
        length = len(popV)
        for i in range(length):
            res = False
            popVal = popV[i]
            if fuzhu and popVal == fuzhu[-1]:
                fuzhu.pop()
                res = True
            else:
                while pushV:
                    val = pushV.pop(0)
                    fuzhu.append(val)
                    if val == popVal:
                        fuzhu.pop()
                        res = True
                        break
            if res == False:
                return res
        return True

