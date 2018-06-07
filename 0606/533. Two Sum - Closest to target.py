class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        if len(nums) < 2:
            return -1
        nums.sort()
        left, right = 0, len(nums) - 1
        min_diff = 65535 # MAX_INT
        while left < right:
            value = nums[left] + nums[right]
            if value < target:
                min_diff = min(min_diff, target-value)
                left += 1
            elif value == target:
                return 0
            else: # value >  target
                min_diff = min(min_diff, value-target)
                right -= 1
        return min_diff

if __name__ == "__main__":
    nums, target = [-1,2,1,-4], 4
    print Solution().twoSumClosest(nums, target)