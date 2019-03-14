# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        import ctypes
        num1 = ctypes.c_int32(num1).value
        num2 = ctypes.c_int32(num2).value
        majority = num1 ^ num2
        carry = (num1 & num2) << 1

        majority = ctypes.c_int32(majority).value
        carry = ctypes.c_int32(carry).value
        if not carry:
            return majority
        else:
            return self.Add(majority, carry)

        return num1
