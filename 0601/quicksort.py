class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def quicksort(self, nums, lo=None, hi=None):# Your submission beats 67.20% Submissions!
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi
        if lo < hi:
            p = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, p-1)
            self.quicksort(nums, p+1, hi)

    def quickselect(self, nums, k, lo=None, hi=None):
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
        nums[pvt], nums[hi] = nums[hi], nums[pvt]
        return pvt

if __name__ == "__main__":
    nums = [1,5,4,2,1,3,2,1,4,2,12,3,2,2,2]
    print Solution().quickselect(nums, 10)
    Solution().quicksort(nums)
    print nums