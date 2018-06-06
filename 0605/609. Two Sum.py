class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5_method1(self, nums, target):
        n = len(nums)
        if n <= 0:
            return 0
        nums.sort()
        count = 0
        for i in range(n):
            for j in range(n-1, i, -1):
                if nums[i] + nums[j] > target:
                    continue
                count += j - i
                break
        return count

    def twoSum5(self, nums, target):
        # Write your code here
        l, r = 0, len(nums) - 1
        cnt = 0
        nums.sort()
        while l < r:
            value = nums[l] + nums[r]
            if value > target:
                r -= 1
            else:
                cnt += r - l
                l += 1
        return cnt


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 24
    from timeit import timeit
    print timeit("Solution().twoSum5(nums, target)",
           setup="from __main__ import Solution, nums, target", number=10000)
    print timeit("Solution().twoSum5_method1(nums, target)",
           setup="from __main__ import Solution, nums, target", number=10000)
