# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        last = first  # 这样复制，修改val或者next都会互相影响

        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and pHead.val == val:
                    pHead = pHead.next
                last.next = pHead  # 但last指针位置不变，以防3,3,4,4的情况出现
            else:
                last.next = pHead
                last = last.next
                pHead = pHead.next
        return first.next