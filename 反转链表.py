# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 递归
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:  # 空链表或最后一个结点
            return pHead
        pNew = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return pNew
# 非递归
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        left = None
        cur = pHead
        while cur:
            right = cur.next
            cur.next = left
            left = cur
            cur = right
        return left
