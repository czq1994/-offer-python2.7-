# -# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) \
               + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        s = s.split(',')
        return self.deserialize(s)

    def deserialize(self, s):
        root = None
        nodeVal = s.pop(0)
        if nodeVal != '#':
            root = TreeNode(int(nodeVal))
            root.left = self.deserialize(s)
            root.right = self.deserialize(s)
        return root  # 当nodeVal=='#'时返回的是None