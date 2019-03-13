# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.res = []
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        if listNode.next != None:
            self.printListFromTailToHead(listNode.next)
        self.res.append(listNode.val)
        return self.res