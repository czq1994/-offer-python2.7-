# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        curSum = None
        maxSum = None
        for i in range(len(array)):
            if not curSum:
                curSum = maxSum = array[i] #首元素
            else:
                if curSum < 0: #若之前的和是负数，则没有累加的必要，先清零再重新开始累加
                    curSum = 0
                curSum += array[i]
                maxSum = max(curSum, maxSum)
        return maxSum