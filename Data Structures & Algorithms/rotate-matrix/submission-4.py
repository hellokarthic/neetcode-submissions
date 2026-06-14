class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i, j = 0, 0
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            i, j = 0, len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i+=1
                j-=1
