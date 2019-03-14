# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
        # return self.stack1
    def pop(self):
        # return xx
        if len(self.stack2) == 0:
            while self.stack1:
                a = self.stack1.pop()
                self.stack2.append(a)
        # 如果不等于0 就这样直接弹出
        return self.stack2.pop()
'''
# 另一种比较麻烦的做法
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        xx = self.stack2.pop()
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append(val)
        return xx
'''