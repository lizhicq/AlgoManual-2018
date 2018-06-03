class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        start, end = 0, len(nums) - 1
        while start < end :
            csum = nums[start] + nums[end]
            if csum == target:
                return [start+1, end+1]
            elif csum < target:
                start += 1
            else:
                end -=1
        return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print Solution().twoSum(nums, target)