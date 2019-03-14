class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols + j] == path[0]:
                    if self.find_path(list(matrix), rows, \
                                      cols, path[1:], i, j):
                        return True

    def find_path(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols + j] = 0
        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j+1)
        elif j-1 >= 0 and matrix[i*cols+j-1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j-1)
        elif i+1 < rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i+1, j)
        elif i-1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i-1, j)
        else:
            return False