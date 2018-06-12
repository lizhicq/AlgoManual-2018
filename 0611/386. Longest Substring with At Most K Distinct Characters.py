class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        j = 0
        ch_set = set()
        ans = 0
        for i in range(len(s)):
            while j < len(s) and len(ch_set) <= k:
                ch_set.add(s[j])
                j += 1
            if len(ch_set) <= k:
                ans = max(ans, j-i)
            ch_set.remove(s[i])
        return ans

if __name__ =="__main__":
    s = "eceba"
    k = 3
    print Solution().lengthOfLongestSubstringKDistinct(s, k)
