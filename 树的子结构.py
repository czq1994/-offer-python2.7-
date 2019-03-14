# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.cmp(pRoot1, pRoot2)  # 这里不应该返回，这样做固定了起点
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2) \
                     or self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def cmp(self, pRoot1, pRoot2):  # 判断两个树是否相等
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.cmp(pRoot1.left, pRoot2.left) and \
               self.cmp(pRoot1.right, pRoot2.right)
