class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        j = 0
        ch_dic = {}
        ans = 0
        for i in range(len(s)):
            while j < len(s):
                if s[j] in ch_dic:
                    ch_dic[s[j]] += 1
                else:
                    if len(ch_dic) == k:
                        break
                    ch_dic[s[j]] = 1
                j += 1

            ans = max(ans, j-i)
            if s[i] in ch_dic:
                if ch_dic[s[i]] > 1:
                    ch_dic[s[i]] -= 1
                else:
                    ch_dic.pop(s[i])
        return ans

if __name__ =="__main__":
    s = "eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh"
    k = 16
    print Solution().lengthOfLongestSubstringKDistinct(s, k)
