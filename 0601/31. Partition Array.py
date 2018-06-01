class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        pvt = 0
        while pvt < len(nums):
            if nums[pvt] == k:
                break
            pvt += 1
        if pvt == len(nums):
            return - 1
        nums[pvt], nums[-1] = nums[-1], nums[pvt]
        pvt = self.partition(nums, 0, len(nums)-1)
        return pvt

    def partition(self, nums, lo, hi):
        pvt = lo
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[i], nums[pvt] = nums[pvt], nums[i]
                pvt += 1
        nums[pvt], nums[hi] = nums[hi], nums[pvt]
        return pvt

if __name__ == "__main__":
    nums = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
    print Solution().partitionArray(nums, 9)
    #print Solution().partition([3, 1, 3, 3, 2, 2], 0, 5)


