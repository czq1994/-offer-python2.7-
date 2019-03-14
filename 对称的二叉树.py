# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        pRoot1 = pRoot
        return self.isSymmetrical2(pRoot, pRoot1)

    def isSymmetrical2(self, pRoot, pRoot1):
        if not pRoot and not pRoot1:
            return True
        if not pRoot or not pRoot1:
            return False
        if pRoot.val != pRoot1.val:
            return False
        else:
            return self.isSymmetrical2(pRoot.left, pRoot1.right) and \
                   self.isSymmetrical2(pRoot.right, pRoot1.left)
