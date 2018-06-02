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