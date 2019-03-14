# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or not size or len(num) < size:
            return [] #特殊情况
        if size == 1: #特殊用例
            return num
        res = []
        ls = [0] # 建立一双向队列,队列中存储num元素的下标
        for i in range(1, len(num)):
            # 当前队列的头结点已经不在滑窗范围内
            if i - ls[0] >= size:
                ls.pop(0) #弹出队首
            # 要插入的值和队尾元素比较，若大于队尾，依次删除，重复比较，最后插入当前元素
            if num[i] < num[ls[-1]] and len(ls) < size:
                ls.append(i)
            elif num[i] >= num[ls[-1]]:
                while ls and num[i] >= num[ls[-1]]:
                    # 这个and前后的顺序不能改变 ！否则会报错
                    # 由于ls的长度最大是size，因此这个循环最多执行size次
                    ls.pop()
                ls.append(i)
            # 要插入的元素比队尾小，且队列长度小于size(其实队列长度必然小于size)

            # 存储每个窗口的最大值
            if i >= size-1:
                res.append(num[ls[0]])
        return res