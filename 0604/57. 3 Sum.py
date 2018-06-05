class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        res = []
        numbers.sort()
        self.dfs([], 0, res, numbers)
        return res

    def dfs(self, tmp, start_index, res, S):
        #print tmp, start_index
        if len(tmp) == 3:
            if sum(tmp) == 0:
                #print tmp, start_index
                res.append(tuple(tmp))
            #print 'return'
            return
        for i in range(start_index, len(S)):
            if i == start_index or S[i-1] != S[i]: # duplicate or not ?
                self.dfs(tmp + [S[i]], i+1, res, S)

if __name__ == "__main__":
    nums = [-11, -7, -5, -4, -4, -3, -3, -2, -2, -1, -1, 1, 2, 3, 4, 5, 5, 7]
    print Solution().threeSum(nums)