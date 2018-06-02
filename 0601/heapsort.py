class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def heapsort(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi

        # 1. build the heap
        for i in range(hi//2, lo-1, -1):
            self.maxheapify(nums, i, hi)
        # 2. delete top
        for i in range(hi, lo, -1):
            nums[lo], nums[i] = nums[i], nums[lo]
            # after each iteration, largest goes to ith, next end at i-1
            self.maxheapify(nums, lo, i-1)

    def maxheapify(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi
        parent = lo
        while parent <= hi:
            left = parent * 2 + 1
            right = parent * 2 + 2
            child = -1

            if left <= hi and right <= hi:
                child = left if nums[left] > nums[right] else right
            elif left <= hi:
                child = left
            else:
                return
            # max heap root >= left and root >= right
            if nums[parent] >= nums[child]:
                return
            nums[parent], nums[child] = nums[child], nums[parent]
            parent = child



if __name__ == "__main__":
    nums = [1,5,4,2,1,3,2,1,4,2,12,3,2,2,2]
    # build maxheap
    s = Solution()
    s.heapsort(nums)
    print nums