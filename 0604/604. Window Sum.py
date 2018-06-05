class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        n = len(nums)
        if n < k or k <= 0:
            return []
        ksum = []
        sums = [0]

        for i in range(1, len(nums)+1):
            sums.append(sums[i-1] + nums[i-1])
            if i >= k:
                ksum.append(sums[i]-sums[i-k])
        return ksum


class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        n = len(nums)
        if n < k or k <= 0:
            return []
        ksum = [0 for i in range(n-k+1)]
        sums = [0 for i in range(n+1)]

        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]
            if i >= k:
                ksum[i-k] = sums[i] - sums[i-k]
        return ksum
if __name__ == "__main__":
    nums = [1,2,7,7,2]
    k = 3
    print Solution().winSum(nums, k)