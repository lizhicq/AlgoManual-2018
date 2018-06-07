class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        S.sort()
        left, right = 0, len(S) - 1
        ans = 0
        for i in range(len(S)):
            left, right = 0, i-1
            while left < right:
                if S[left] + S[right] > S[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 5, 7]
    print Solution().triangleCount(nums)