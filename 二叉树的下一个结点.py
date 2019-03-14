# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        # 若有右子节点，顺着右子节点找到最左的叶子节点
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        # 若没有叶子结点
        else:
            # 若有父节点且是父节点的左子节点
            if pNode.next and pNode == pNode.next.left:
                return pNode.next
            # 若有父节点且是父节点的右子节点
            elif pNode.next and pNode == pNode.next.right:
                node = pNode.next
                while node:
                    if node.next and node == node.next.left:
                        return node.next
                    node = node.next
        return None
