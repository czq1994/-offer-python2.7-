# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        # 1. 判断是否有环,若有，记录下环内节点个数
        pHead1 = pHead  # 快指针，一次走两步
        pHead2 = pHead  # 慢指针，一次走一步
        mark = 0  # 记录是否有环
        count = 0
        while pHead1.next:
            count += 1
            pHead1 = pHead1.next.next
            pHead2 = pHead2.next
            if pHead1 == pHead2:
                mark = 1
                break
        if not mark:
            return None  # 没有环
        countNum = count
        # 2.找到环的入口节点
        pHead1 = pHead
        while countNum:
            pHead1 = pHead1.next
            countNum -= 1
        while 1:
            if pHead == pHead1:
                return pHead
            pHead = pHead.next
            pHead1 = pHead1.next
