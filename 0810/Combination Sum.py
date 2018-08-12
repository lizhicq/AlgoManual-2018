class Solution(object):
    def consum(self, nums, target):

        nums.sort()
        res = []
        def dfs(start, tmp):
            cum = sum(tmp)
            if cum > target or start == len(nums):
                return
            if cum == target:
                res.append(tmp)
                return
            for i in range(start, len(nums)):
                dfs(i, tmp + [nums[i]])

        dfs(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print s.consum([2,3,6,7], 7)


