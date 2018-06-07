class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        return self.quickselect(k-1, nums)

    def quickselect(self, k, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi
        while True:
            if lo == hi:
                return nums[lo]
            pvt = self.partition(nums, lo, hi)
            if k == pvt:
                return nums[k]
            elif k < pvt:
                hi = pvt - 1
            else:
                lo = pvt + 1

    def partition(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi
        pvt = lo
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[i], nums[pvt] = nums[pvt], nums[i]
                pvt += 1
        nums[hi], nums[pvt] = nums[pvt], nums[hi]
        return pvt


if __name__ == "__main__":
    k, nums = 3, [2,3,4,8,9]
    print Solution().kthSmallest(k, nums)