class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        out = []
        for i in range(n):
            res2 = []
            for j in range(n-1, -1, -1):
                res2.append(matrix[j][i])
            out.append(res2)
        matrix[:] = out