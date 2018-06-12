class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize1(self, nums, s): # 34.40%
        n = len(nums)
        if n == 0 or sum(nums) < s:
            return -1
        start, end = 1, n
        cum = [0]
        for i in range(1, n+1):
            cum.append(nums[i-1] + cum[i-1])
        def check(k):  # k is large enough
            for i in range(len(nums) - k + 1):
                if cum[i+k] - cum[i] >= s:
                    return True
            return False

        while start + 1 < end:
            mid = start + (end - start) // 2
            if check(mid):
                end = mid
            else:
                start = mid

        if check(start):
            return start
        if check(end):
            return end
        return -1

    def minimumSize(self, nums, s): # 34.40%
        from sys import maxsize
        i = j = 0
        cum = 0
        ans = maxsize
        for i in range(len(nums)):
            while j < len(nums) and cum < s:
                cum += nums[j]
                j += 1
            if cum >= s:
                ans = min(ans, j-i)
            cum -= nums[i]

        return ans if ans != maxsize else -1


if __name__ == "__main__":
    nums = [100,50,99,50,100,50,99,50,100,50]
    s = 250
    print Solution().minimumSize(nums, s)