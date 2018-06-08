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

if __name__ =="__main__":
    S = [1, 0, -1, 0, -2, 2]
    target = 0
    print Solution().fourSum2(S, target)
    from timeit import timeit
    count = 0
    for i in range(100):
        a = timeit("Solution().fourSum1(S, target)",
                 setup="from __main__ import Solution, S, target", number=100)
        b = timeit("Solution().fourSum2(S, target)",
                 setup="from __main__ import Solution, S, target", number=100)
        count += 1 if a < b else 0
    print count
