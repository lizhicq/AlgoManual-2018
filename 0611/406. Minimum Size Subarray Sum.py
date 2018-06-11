class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if len(nums) == 0:
            return -1
        import heapq
        heapq._heapify_max(nums)
        csum = 0
        count = 0
        while nums:
            csum += heapq._heappop_max(nums)
            count += 1
            if csum >= s:
                return count
        return -1