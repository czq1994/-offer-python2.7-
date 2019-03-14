# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def Convert(self, pRootOfTree):
        # write code here#左节点是中序遍历的上一个节点，右节点是中序遍历的下一个节点
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        # 对结点进行操作，首先head, tail共同指向最左边（即最小）的叶结点，
        # 然后tail慢慢后移，head不变
        if not self.head:
            self.head = pRootOfTree
            self.tail = pRootOfTree
        else:
            self.tail.right = pRootOfTree
            pRootOfTree.left = self.tail
            self.tail = pRootOfTree
        self.Convert(pRootOfTree.right)

        return self.head
