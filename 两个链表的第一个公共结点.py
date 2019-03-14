# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 先计算两个链表的长度，找出长度差。
    # 然后让指针现在长链表上走出长度差的距离
    def FindFirstCommonNode(self, pHead1, pHead2):
        node1 = pHead1
        node2 = pHead2
        count1 = count2 = 0
        while node1:
            count1 += 1
            node1 = node1.next
        while node2:
            count2 += 1
            node2 = node2.next
        count_dif = count1 - count2
        if count_dif > 0:
            longList = pHead1
            shortList = pHead2
        else:
            count_dif = -count_dif
            longList = pHead2
            shortList = pHead1
        while count_dif:
            longList = longList.next
            count_dif -= 1
        while longList and shortList:
            if longList == shortList:
                return longList
            longList = longList.next
            shortList = shortList.next
        return None
