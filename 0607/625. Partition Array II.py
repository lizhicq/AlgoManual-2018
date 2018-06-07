class Solution:
    """
    @param: nums: an integer array
    @param: low: An integer
    @param: high: An integer
    @return:
    """
    def partition2(self, nums, low, high):
        left, right = 0, len(nums) - 1
        i = 0
        while i < right:
            if nums[i] < low:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] > high:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        return nums

if __name__ == "__main__":
    nums, low, high = [4,3,4,1,2,3,1,2], 2, 3
    print Solution().partition2(nums, low, high)
