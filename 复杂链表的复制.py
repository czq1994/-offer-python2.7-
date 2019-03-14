# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        pHead1 = pHead
        while pHead1:
            pClone = RandomListNode(pHead1.label)
            pClone.next = pHead1.next
            pHead1.next = pClone
            pHead1 = pClone.next

        pHead2 = pHead
        while pHead2:
            clone = pHead2.next
            raw = pHead2
            if raw.random:  # 这句话不加会出问题的
                clone.random = raw.random.next
            pHead2 = pHead2.next.next

        # 进行拆分,这个地方要注意，我很容易出错
        pNode = pHead
        pCloneNode = pNode.next
        pCloneHead = pCloneNode

        pNode.next = pCloneNode.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next

            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead
