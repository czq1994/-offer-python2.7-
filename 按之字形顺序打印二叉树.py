# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        resRow = []
        ls = []
        ls.append(pRoot)
        # =====初始化3个标记变量==============
        mark = 1  # 1:从左往右， -1:从右往左
        toPrint = 1
        if pRoot.left and pRoot.right:
            nextLevel = 2
        elif pRoot.left or pRoot.right:
            nextLevel = 1
        else:
            nextLevel = 0
        # ============主体循环============
        while ls:
            curNode = ls.pop(0)
            resRow.append(curNode.val)
            toPrint -= 1
            if toPrint == 0:
                if mark > 0:
                    res.append(resRow[:])
                else:
                    resRow.reverse()
                    res.append(resRow[:])
                mark = -mark
                toPrint = nextLevel
                nextLevel = 0
                resRow = []
            if curNode.left:
                ls.append(curNode.left)
                nextLevel += 1
            if curNode.right:
                ls.append(curNode.right)
                nextLevel += 1
        return res
