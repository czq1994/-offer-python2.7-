# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        #循环，判断是否为偶数，若是，在列表中删除该元素，同时列表末尾添加该元素
        #需要加mask来判断是否又回到了最初添加在末尾的第一个偶数元素，若是，则停止循环
        left = [x for x in array if x & 1 == 1]
        right = [x for x in array if x & 1 == 0]
        return left + right