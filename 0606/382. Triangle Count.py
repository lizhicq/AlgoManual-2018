class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        S.sort()
        self.count = 0

        def dfs(tmp, start_index):
            # print tmp, start_index
            if len(tmp) == 3:
                if tmp[0] + tmp[1] > tmp[2]:
                    self.count += 1
                return
            for i in range(start_index, len(S)):
                dfs(tmp + [S[i]], i + 1)

        dfs([], 0)
        return self.count



if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 5, 7]
    print Solution().triangleCount(nums)