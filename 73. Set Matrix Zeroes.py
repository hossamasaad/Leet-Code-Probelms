class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        iS, jS = [], []
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    iS.append(i)
                    jS.append(j)
        
        for i in range(n):
            if i in iS:
                matrix[i] = [0] * m
            else:
                for j in range(m):
                    if j in jS:
                        matrix[i][j] = 0
                