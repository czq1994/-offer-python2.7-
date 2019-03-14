# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k < 1 or not pRoot:
            return None
        self.res = []
        self.midOrder(pRoot)
        if len(self.res) < k:
            return None
        else:
            return self.res[k - 1]

        # 中序遍历即为递增

    def midOrder(self, pRoot):
        if not pRoot:
            return

        self.midOrder(pRoot.left)
        self.res.append(pRoot)
        self.midOrder(pRoot.right)

