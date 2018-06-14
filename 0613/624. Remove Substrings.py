class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        #from Queue import Queue
        que = []
        str_set = set()

        que.append(s)
        str_set.add(s)
        ans = len(s)
        while len(que) > 0:
            s = que.pop()
            for sub in dict:
                found = s.find(sub)
                while found != -1:
                    new_s = s[:found] + s[found+len(sub):]
                    if new_s not in str_set:
                        str_set.add(new_s)
                        ans = min(ans, len(new_s))
                        que.append(new_s)
                        str_set.add(new_s)
                    found = s.find(sub, found + 1)

        return ans
if __name__ == "__main__":
    s = "ccdaabcdbb"
    dict = ["ab", "cd"]
    print Solution().minLength(s, dict)