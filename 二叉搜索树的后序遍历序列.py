class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        mark = True
        rootVal = sequence[-1]
        length = len(sequence)
        # 左子树要比rootVal小，找到第一个比rootVal大的
        # 如果没有找到的话，表明没有右子树，i为列表最后一个值的下标,此时下一个循环直接跳过
        for i in range(length):
            if sequence[i] > rootVal:
                break
        for j in range(i, length - 1):
            if sequence[j] < rootVal:
                return False
        left = sequence[:i]
        right = sequence[i:-1]
        if left and right:
            mark = self.VerifySquenceOfBST(left) \
                   and self.VerifySquenceOfBST(right)
        elif left:
            mark = self.VerifySquenceOfBST(left)
        elif right:
            mark = self.VerifySquenceOfBST(right)
        return mark
