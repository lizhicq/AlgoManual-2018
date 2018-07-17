class maxheap(object):

    def heapsort(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums) if hi is None else hi
        self.heapify(nums)
        for i in range(hi, lo, -1):
            nums[lo], nums[i] = nums[i], nums[lo]
            self.shiftdown(nums, lo, i-1)

    def heapify(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums)-1 if hi is None else hi
        for i in range(hi//2, lo-1, -1):
            self.shiftdown(nums, i, hi)

    def heappush(self, nums, val, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums)-1 if hi is None else hi
        hi += 1
        nums.insert(hi, val)
        self.shiftup(nums, lo, hi)

    def heappop(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums)-1 if hi is None else hi
        nums[lo], nums[hi] = nums[hi], nums[lo]
        self.shiftdown(nums, lo, hi-1)
        return nums.pop(hi)

    def shiftdown(self, nums, lo=None, hi=None): # shift root to proper pos
        lo = 0 if lo is None else lo
        hi = len(nums) if hi is None else hi
        parent = lo
        while parent < hi:
            left = parent * 2 + 1
            right = parent * 2 + 2
            if right <= hi:
                child = left if nums[left] > nums[right] else right
            elif left <= hi:
                child = left
            else:
                return
            if nums[parent] >= nums[child]:
                return
            nums[parent], nums[child] = nums[child], nums[parent]
            parent = child

    def shiftup(self, nums, lo=None, hi=None): # shift hi to proper
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi
        child = hi
        while child > lo:
            parent = child // 2
            if parent < lo or nums[parent] >= nums[child]:
                return
            nums[parent], nums[child] = nums[child], nums[parent]
            child = parent

