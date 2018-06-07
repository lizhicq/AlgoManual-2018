class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum7(self, nums, target):
        # Write your code here
        dct = {}
        for i in range(len(nums)):
            if nums[i] - target in dct:
                return (dct[nums[i] - target] + 1, i + 1)
            if nums[i] + target in dct:
                return (dct[nums[i] + target] + 1, i + 1)
            dct[nums[i]] = i ## 5+5 = 10?


if __name__ == "__main__":
    print Solution().twoSum7([2, 7, 15, 24], 5)