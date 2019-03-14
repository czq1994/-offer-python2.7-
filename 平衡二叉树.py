# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.IsBalanced(pRoot)[1]
    def IsBalanced(self, pRoot):
        #global mark
        if not pRoot:
            return 0, True
        left, mark1 = self.IsBalanced(pRoot.left)
        right, mark2 = self.IsBalanced(pRoot.right)
        if mark1 & mark2:
            if abs(left - right) <= 1:
                return max(left, right)+1, True
        return 1, False

'''
class Solution:
    def IsBalanced_Solution(self, pRoot):
        global mark
        mark = True
        self.IsBalanced(pRoot)
        return mark
    def IsBalanced(self, pRoot):
        global mark
        if not pRoot:
            return 0
        left = self.IsBalanced(pRoot.left)
        right = self.IsBalanced(pRoot.right)
        if abs(left - right) > 1:
            mark = False
        return max(left, right)+1
'''