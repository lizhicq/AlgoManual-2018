class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6_method1(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            value = nums[left] + nums[right]
            if value < target:
                left += 1
            elif value == target:
                if left == 0 or nums[left-1] != nums[left]:
                    count += 1
                left += 1
            else: # value > target
                right -= 1
        return count
    def twoSum6(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            value = nums[left] + nums[right]
            if value < target:
                left += 1
            elif value == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            else: # value > target
                right -= 1
        return count

if __name__ == "__main__":
    nums, k = [1,1,2,45,46,46], 47
    print Solution().twoSum6(nums, k)
    from timeit import timeit
    print timeit("Solution().twoSum6_method1(nums, k)",
                 setup="from __main__ import nums, k, Solution", number=10000)
    print timeit("Solution().twoSum6(nums, k)",
                 setup="from __main__ import nums, k, Solution", number=10000)