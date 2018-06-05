class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    # method1
    def kthLargestElement(self, k, A):
        # method 1
        # return self.quickselect(A, len(A)-k)
        # method 2
        import heapq
        heapq.heapify(A)
        return heapq.nlargest(k, A)[-1]

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
        if lo >= hi: return lo
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
    k = 10
    A = [1,2,3,4,5,6,8,9,10,7]
    print Solution().kthLargestElement(k, A)
    from test5 import k, A
    print Solution().kthLargestElement(k, A)