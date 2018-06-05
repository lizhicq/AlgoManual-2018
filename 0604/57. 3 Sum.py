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

    def dfs(self, tmp, start_index, res, numbers):
        print tmp, start_index
        if len(tmp) == 3:
            if sum(tmp) == 0:
                #print tmp, start_index
                res.append(tuple(tmp))
            return
        for i in range(start_index, len(numbers)):
            self.dfs(tmp + [numbers[i]], start_index+1, res, numbers)

if __name__ == "__main__":
    print Solution().threeSum([-4, 1, 2])