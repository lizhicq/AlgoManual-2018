from sys import maxint
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit1(self, prices):
        profit = 0
        low = maxint
        for price in prices:
            profit = max(profit, price-profit)
            low = min(low, price)
        return profit

    def maxProfit2(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            profit += max(prices[i+1]-prices[i], 0)
        return profit

    def maxProfit3(self, prices):
        profit = []
        for i in range(len(prices)-1):
            profit.append(prices[i+1] - prices[i])

        return max(self.maxTwoSubArrays(profit), 0)

    def maxProfit4(self, k, prices):
        profits = []
        count_postive = 0
        cum = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            profits.append(prices[i + 1] - prices[i])
            if profit > 0:
                count_postive += 1
                cum += profit

        if len(profits) <= k or count_postive <= k:
            return cum

        return max(self.maxSubArray(profits, k), 0)

    def maxTwoSubArrays(self, nums):
        if len(nums) == 1:
            return nums[0]
        # at least there should be 2 elements in nums
        # If you need to add/remove at both ends, consider using a collections.deque instead.
        left_max = [0 for i in range(len(nums))]
        max_sum = cur_sum = left_max[0] = nums[0]

        for i in range(1, len(nums) - 1):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
            left_max[i] = max_sum

        right_max = [0 for i in range(len(nums))]
        max_sum = cur_sum = right_max[-1] = nums[-1]

        for i in range(len(nums) - 2, 0, -1):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
            right_max[i] = max_sum

        max_sum = - maxint
        for i in range(0, len(nums) - 1):
            max_sum = max(max_sum, left_max[i] + right_max[i + 1])

        return max_sum

    def maxSubArray(self, nums, k):
        f = [[[-maxint for t in range(2)]
              for j in range(k + 1)]
             for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            f[i][0][0] = 0
        for j in range(1, k + 1):
            f[j][j][1] = sum(nums[:j])
            for i in range(j + 1, len(nums) + 1):
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1])
                f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0],
                                 f[i - 1][j - 1][1]) + nums[i - 1]

        return max(f[-1][-1])


if __name__ =="__main__":
    s = Solution()
    print s.maxProfit4(9, [12,3,7,4,5,13,2,8,4,7,6,5,7])