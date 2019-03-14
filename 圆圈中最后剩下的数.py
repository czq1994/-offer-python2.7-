# -*- coding:utf-8 -*-
class listNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_


class Solution:
    def get_circle(self, n):
        node = listNode(0)
        root = node
        for i in range(n - 1):
            node.next_ = listNode(i + 1)
            node = node.next_
        node.next_ = root
        return root

    def del_node(self, root, m):  # 删除第m个结点，将第m+1个结点设为头结点，返回
        count = 0
        while count < m - 2:
            root = root.next_
            count += 1
        root.next_ = root.next_.next_  # 删除第m个结点
        root = root.next_
        return root

    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1:
            return -1
        root = self.get_circle(n)
        while root.next_ != root:
            root = self.del_node(root, m)
        return root.val
