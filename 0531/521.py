class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        nums = list(set(nums))
        return len(nums)

    def deduplication2(self, nums):
        nums.sort()
        pvt = 0
        for i in range(len(nums)):
            if nums[i] != nums[pvt]:
                pvt += 1
                nums[pvt] = nums[i]
        return pvt + 1
