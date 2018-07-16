class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        lo = 0
        hi = len(A) - 1
        for i in range(hi//2, lo-1, -1):
            self.minheapify(A, i, hi)


    def minheapify(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums)-1 if hi is None else hi
        parent = lo
        while parent <= hi:
            left = parent * 2 + 1
            right = parent * 2 + 2
            if right <= hi:
                child = left if nums[left] < nums[right] else right
            elif left <= hi:
                child = left
            else:
                return
            if nums[parent] <= nums[child]:
                return
            nums[parent], nums[child] = nums[child], nums[parent]
            parent = child

if __name__ == "__main__":
    import heapq, random
    s = Solution()
    nums1 = random.sample(range(100), 30)
    nums2 = nums1[:]
    heapq.heapify(nums1)
    s.heapify(nums2)
    print nums1
    print nums2