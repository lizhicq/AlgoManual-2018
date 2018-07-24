class Solution(object):
    def submatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0 for j in range(n+1)]
                       for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                self.sum[i][j] = matrix[i-1][j-1] + self.sum[i][j-1] \
                               + self.sum[i-1][j] - self.sum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2+1][col2+1] - self.sum[row1][col2+1] \
                - self.sum[row2+1][col1] + self.sum[row1][col1]


if __name__ == "__main__":
    s = Solution()
    print s.submatrixSum([[1,5,7],[3,7,-8],[4,-8,9]])