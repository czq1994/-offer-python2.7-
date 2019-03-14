# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while rows > 2 * start and cols > 2 * start:
            endx = rows - 1 - start
            endy = cols - 1 - start
            for i in range(start, endy + 1):
                result.append(matrix[start][i])
            if start < endx:
                for i in range(start + 1, endx + 1):
                    result.append(matrix[i][endy])
            if start < endx and start < endy:
                for i in range(endy - 1, start - 1, -1):
                    result.append(matrix[endx][i])
            if start < endx - 1 and start < endy:
                for i in range(endx - 1, start, -1):
                    result.append(matrix[i][start])

            start += 1
        return result
