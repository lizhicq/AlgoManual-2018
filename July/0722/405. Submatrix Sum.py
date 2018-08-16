class Solution(object):
    def submatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        sums = [[0 for j in range(n+1)]
                       for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                sums[i][j] = matrix[i-1][j-1] + sums[i][j-1] \
                               + sums[i-1][j] - sums[i-1][j-1]
        print sums
        for l in range(m):
            for h in range(l+1, m+1):
                map = {}
                for j in range(n+1):
                    diff = sums[h][j] - sums[l][j]
                    if diff in map:
                        k = map[diff]
                        print diff, k, j, h, l
                        return [[l, k], [h-1, j-1]]
                    else:
                        map[diff] = j

if __name__ == "__main__":
    s = Solution()
    print s.submatrixSum([[1,5,7],[3,7,-8],[4,-8,9]])