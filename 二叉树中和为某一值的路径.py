# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        res = []
        curPath = []
        return self.findpath(root, expectNumber, curPath, res)

    def findpath(self, root, expectNumber, curPath, res):
        curPath.append(root.val)
        if not root.left and not root.right:
            if sum(curPath) == expectNumber:
                res.append(curPath)
        if root.left:
            self.findpath(root.left, expectNumber, curPath[:], res)
        if root.right:
            self.findpath(root.right, expectNumber, curPath[:], res)
        return res

