class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        sums = [[0 for j in range(n+1)]
                       for i in range(m+1)]
        self.arr = matrix
        self.m, self.n = m, n
        for i in range(1, m+1):
            for j in range(1, n+1):
                sums[i][j] = matrix[i-1][j-1] + sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1]

    def update(self, sums, row, col ,val):
        delta = val - self.arr[row][col]
        self.arr[row][col] = val
        i, j = row+1, col+1
        while i <= self.m:
            while j <= self.n:
                sums[i][j] += delta
                j += self.lowbit(j)
            i += self.lowbit(i)
    def lowbit(self, i):
        return i & (-i)

    def sumRegion(self, sums, row1, col1, row2, col2):
        return sums[row2+1][col2+1] - sums[row1][col2+1] - sums[row2+1][col1] + sums[row1][col1]