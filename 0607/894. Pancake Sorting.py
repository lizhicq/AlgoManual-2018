class FlipTool:
    @classmethod
    def flip(cls, arr, i):
        left, right = 0, i
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -=1

class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, arr):
        cur_size = len(arr) - 1
        while cur_size > 1:
            mi = self.findMax(arr, cur_size)
            FlipTool.flip(arr, mi)
            FlipTool.flip(arr, cur_size-1)
            cur_size -= 1
        return arr

    def findMax(self, arr, n):
        mi = 0
        for i in range(n):
            mi = i if arr[i] > arr[mi] else mi
        return mi

if __name__ == "__main__":
    nums = [6, 11, 10, 7, 12, 20, 2]
    print Solution().pancakeSort(nums)