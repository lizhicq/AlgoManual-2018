class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        n = len(nums)
        self.quickselect(nums, n-k)
        return sorted(nums[n-k:], reverse=True)


    def quickselect(self, nums, k, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums)-1 if hi is None else hi
        while True:
            if lo == hi:
                return nums[lo]
            pvt = self.partition(nums, lo, hi)
            if k == pvt:
                return nums[k]
            elif pvt > k:
                hi = pvt - 1
            else:
                lo = pvt + 1

    def partition(self, nums, lo=None, hi=None):
        lo = 0 if lo is None else lo
        hi = len(nums)-1 if hi is None else hi

        pvt = lo
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[i], nums[pvt] = nums[pvt], nums[i]
                pvt += 1
        nums[hi], nums[pvt] = nums[pvt], nums[hi]
        return pvt


if __name__ == "__main__":
    s = Solution()
    print s.partition([1,2,3,1,5,6,4])
    print s.topk([3,10,1000,-99,4,100], 3)


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        from heapq import heappush, heappop
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        ans = []
        while heap:
            ans.append(heappop(heap))
        return ans[::-1]
