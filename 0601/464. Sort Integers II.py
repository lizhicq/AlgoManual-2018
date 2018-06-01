class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        pass

    def quicksort(self, nums):
        pass

    def partition(self, nums, lo, hi):
        pvt = lo
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[i], nums[pvt] = nums[pvt], nums[i]
                pvt += 1
        nums[pvt], nums[hi] = nums[hi], nums[pvt]
        print nums
        return pvt

    def mergesort(self, nums):
        pass
    def heapsort(self, nums):
        pass


if __name__ == "__main__":
    print Solution().partition([1,2,3,4,5,6,7,5.5], 0, 7)