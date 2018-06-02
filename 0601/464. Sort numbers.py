class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A): # A.sort() Your submission beats 98.00% Submissions!
        A.sort()
        lo, hi = 0, len(A) - 1
        A = self.mergesort(A,lo,hi)
        return A


    def quicksort(self, nums, lo, hi):# Your submission beats 67.20% Submissions!
        if lo < hi:
            p = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, p-1)
            self.quicksort(nums, p+1, hi)

    def quickselect(self, nums, lo, hi, k):
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

    def partition(self, nums, lo, hi):
        pvt = lo
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[i], nums[pvt] = nums[pvt], nums[i]
                pvt += 1
        nums[pvt], nums[hi] = nums[hi], nums[pvt]
        return pvt

    def mergesort(self, nums, lo, hi): # Your submission beats 33.00% Submissions!
        if lo == hi:
            return [nums[lo]]
        mid = (lo + hi) // 2
        left = self.mergesort(nums, lo, mid)
        right = self.mergesort(nums, mid+1, hi)
        return self.merge(left, right)

    def merge(self, left, right): # merge two sorted list
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    def heapsort(self, nums):
        pass



    def heapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[i] < nums[left]:
            largest = left
        if right < n and nums[largest] < nums[right]:
            largest = right
        nums[i], nums[largest] = nums[largest], nums[i]
        self.heapify(nums, n, largest)


from heapq import heapify
if __name__ == "__main__":
    nums = [3,2,1,4,5]
    heapify(nums)
    print nums