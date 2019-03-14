# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        # 这个标记位是关键
        boolVisited = [False] * (rows * cols)
        count = self.main(threshold, rows, cols, 0, 0, boolVisited)
        return count

    def main(self, threshold, rows, cols, row, col, boolVisited):
        count = 0
        if self.check(threshold, rows, cols, row, col, boolVisited):
            boolVisited[row * cols + col] = True
            count = 1 + self.main(threshold, rows, cols, row - 1, col, boolVisited) \
                    + self.main(threshold, rows, cols, row + 1, col, boolVisited) \
                    + self.main(threshold, rows, cols, row, col - 1, boolVisited) \
                    + self.main(threshold, rows, cols, row, col + 1, boolVisited)
        return count

    def check(self, threshold, rows, cols, row, col, boolVisited):
        if (row < rows and row >= 0 and col < cols and col >= 0) \
                and boolVisited[row * cols + col] == False \
                and (self.getDigitSum(row) + self.getDigitSum(col) <= threshold):
            return True
        return False

    def getDigitSum(self, num):
        res = 0
        while num:
            res += num % 10
            num = num // 10
        return res