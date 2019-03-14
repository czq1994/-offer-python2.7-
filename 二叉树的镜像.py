# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        # 先序遍历
        # 递归出口
        if not root:
            return
        # 对根节点的操作，交换左右子树
        node = root.left
        root.left = root.right
        root.right = node
        # 对左右子树递归操作
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
