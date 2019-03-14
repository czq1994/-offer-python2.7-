# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        #两个链表至少有一个为空
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        node = ListNode(-1)
        root = node #保存节点
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
                node = node.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
                node = node.next
        if pHead1:
            node.next = pHead1
        elif pHead2:
            node.next = pHead2
        return root.next