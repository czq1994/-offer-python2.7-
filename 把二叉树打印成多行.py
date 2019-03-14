# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # 用一个队列，与宽度优先遍历不同的是，这道题还需要记录每行的个数
        if not pRoot:
            return []
        toPrint = 1  # 当前层待打印节点数
        nextLevel = 0
        res = []  # 总结果
        rowRes = []  # 每一层
        ls = [pRoot]
        while ls:
            node = ls.pop(0)
            rowRes.append(node.val)
            toPrint -= 1
            if node.left:
                ls.append(node.left)
                nextLevel += 1
            if node.right:
                ls.append(node.right)
                nextLevel += 1
            if toPrint == 0:
                toPrint = nextLevel
                nextLevel = 0
                res.append(rowRes)
                rowRes = []
        return res
