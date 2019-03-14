# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        node1 = head
        node2 = head
        while k:
            if not node1:  # 链表长度小于k
                return None
            node1 = node1.next
            k -= 1
        while node1:
            node1 = node1.next
            node2 = node2.next
        return node2
