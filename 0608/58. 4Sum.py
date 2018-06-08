class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum1(self, S, target):
        S.sort()
        res = []

        def dfs(tmp, index):
            if len(tmp) == 4:
                if sum(tmp) == target:
                    res.append((tmp[0], tmp[1], tmp[2], tmp[3]))
                return
            for i in range(index, len(S)):
                if i == index or S[i-1] != S[i]:
                    dfs(tmp + [S[i]], i+1)

        dfs([], 0)
        return res

    def fourSum2(self, S, target):
        S.sort()
        res = []

        def dfs(tmp, index):
            if len(tmp) == 4:
                if sum(tmp) == target:
                    res.append((tmp[0], tmp[1], tmp[2], tmp[3]))
                return
            for i in range(index, len(S)):
                if i != index and S[i-1] == S[i]:
                    continue
                dfs(tmp + [S[i]], i+1)

        dfs([], 0)
        return res

    def fourSum3(self, nums, target):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res

if __name__ =="__main__":
    S = [1, 0, -1, 0, -2, 2]
    target = 0
    print Solution().fourSum2(S, target)
    from timeit import timeit
    count = 0
    for i in range(100):
        a = timeit("Solution().fourSum1(S, target)",
                 setup="from __main__ import Solution, S, target", number=1000)
        b = timeit("Solution().fourSum2(S, target)",
                 setup="from __main__ import Solution, S, target", number=1000)
        c = timeit("Solution().fourSum3(S, target)",
                 setup="from __main__ import Solution, S, target", number=1000)

        print a, b, c
    print count
