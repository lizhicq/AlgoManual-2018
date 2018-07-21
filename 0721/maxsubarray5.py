# -*- coding: utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums, k):
        from sys import maxsize
        n = len(nums)

        f = [[[-0 for t in range(2)]
                for j in range(k+1)]
                for i in range(n+1)]

        # 如果都设置成0，全是负数的情况下，可以一个都不选
        # 如果都设置成负无穷，负数也必须选。
        ## init dp
        for i in range(1, n+1): # k = 0 仍然可以一个不选为0
            f[i][0][0] = 0
        cumj = 0

        for j in range(1, k+1):
            cumj += nums[j-1]
            f[j][j][1] = cumj
            for i in range(j+1, n+1):
                f[i][j][0] = max(f[i-1][j][0], f[i-1][j][1])
                f[i][j][1] = max(f[i-1][j][1], f[i-1][j-1][0],
                                 f[i-1][j-1][1]) + nums[i-1]
                print i, j, f[i][j]

        return max(f[-1][-1])


if __name__ == "__main__":
    print Solution().maxSubArray([1, -2, 3], 3)
    #print Solution().maxSubArray([-1, 4, -2, 3, -2, 3], 2)