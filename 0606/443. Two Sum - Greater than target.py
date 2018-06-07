class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        if len(nums) < 2:
            return -1
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            value = nums[left] + nums[right]
            if value <= target:
                left += 1
            else:
                count += right - left
                right -= 1
        return count

if __name__ == "__main__":
    nums, target = [2,7,11,15], 24
    print Solution().twoSum2(nums, target)