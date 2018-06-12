class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        i = j = 0
        ch_set = set()
        ans = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in ch_set:
                ch_set.add(s[j])
                j += 1
            ans = max(ans, j-i)
            ch_set.remove(s[i])
        return ans


if __name__ == "__main__":
    s = "abcabcbb"
    print Solution().lengthOfLongestSubstring(s)
