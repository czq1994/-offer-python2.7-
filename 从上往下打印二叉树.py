# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        ls = [root]
        while ls:
            cur = ls.pop(0)
            res.append(cur.val)
            if cur.left:
                ls.append(cur.left)
            if cur.right:
                ls.append(cur.right)
        return res