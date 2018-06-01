class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A): # A.sort() Your submission beats 98.00% Submissions!
        lo, hi = 0, len(A) - 1
        self.quicksort(A, lo, hi)

    def quicksort(self, nums, lo, hi):# Your submission beats 67.20% Submissions!
        if lo < hi:
            p = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, p-1)
            self.quicksort(nums, p+1, hi)

    def quickselect(self, nums, k):
        p = self.partition(nums, 0, len(nums)-1)
        while True:
            print p, nums
            if p == k:
                return nums[p]
            elif p < k:
                p = self.partition(nums, p+1, len(nums)-1)
            else: #p > k
                p = self.partition(nums, 0, p)

    def partition(self, nums, lo, hi):
        pvt = lo
        mid = (lo + hi) // 2
        nums[mid], nums[hi] = nums[hi], nums[mid]
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[i], nums[pvt] = nums[pvt], nums[i]
                pvt += 1
        nums[pvt], nums[hi] = nums[hi], nums[pvt]
        return pvt

    def mergesort(self, nums):
        pass
    def heapsort(self, nums):
        pass


if __name__ == "__main__":
    #print Solution().partition([1,2,3,4,5,6,7,5.5], 0, 7)
    nums = range(10)
    print nums
    for i in range(10):
        print Solution().quickselect(nums, i)