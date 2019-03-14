# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        # if not A:
        #   return None
        length = len(A)
        b = list(range(length))
        b[0] = 1
        tmp = 1
        for i in range(1, length):
            b[i] = b[i - 1] * A[i - 1]

        for i in range(length - 2, -1, -1):
            tmp = tmp * A[i + 1]
            b[i] = b[i] * tmp
        return b
