class Solution(object):
    def mergesort(self, nums, lo=None, hi=None): # Your submission beats 33.00% Submissions!
        lo = 0 if lo is None else lo
        hi = len(nums) - 1 if hi is None else hi
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

if __name__ == "__main__":
    nums = [1, 5, 4, 2, 1, 3, 2, 1, 4, 2, 12, 3, 2, 2, 2]
    print Solution().mergesort(nums)