class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if len(nums) == 0 :
            return None
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums)-1
        last = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == nums[-1]:
                start += 1
            elif nums[mid] > nums[-1]:
                start = mid
            else:
                end = mid
            print start, mid, end
        if nums[start] < nums[-1]:
            return nums[start]
        else:
            return nums[end]

if __name__ == "__main__":
    print Solution().findMin([999,999,1000,1000,10000,0,999,999,999])