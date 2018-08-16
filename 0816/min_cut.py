class Solution(object):

    def minCut(self, S):
        n = len(S)
        f = [n-i-1 for i in range(n+1)]# [n, n-1, ... -1]
        p = [[False for i in range(n)]
                    for j in range(n)] # p[i][j] = True if S[i:j+1] is palindrome

        for i in reversed(range(n)):
            for j in range(i, n):
                if S[i] == S[j] and (j-i < 2 or p[i+1][j-1]):
                    p[i][j] = True
                    f[i] = min(f[i], f[j+1] + 1)
                    print i, j, f
        return f[0]
if __name__ == "__main__":
    s = Solution()
    print s.minCut("aab")