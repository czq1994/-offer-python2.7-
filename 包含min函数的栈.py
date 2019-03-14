# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.fuzhu = []  # 降序

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.fuzhu:
            self.fuzhu.append(node)
        else:
            if node < self.fuzhu[-1]:
                self.fuzhu.append(node)
            else:
                self.fuzhu.append(self.fuzhu[-1])

    def pop(self):
        # write code here
        self.fuzhu.pop()
        return self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.fuzhu[-1]