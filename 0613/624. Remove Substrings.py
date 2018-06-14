class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        if len(dict) == 0:
            return s
        from collections import deque
        deck = deque()
        deck.append(dict[0])
        while len(deck) > 0:
            substr = deck.popleft()
            s = s.replace(substr, "")
            for substr in dict:
                if substr in s:
                    deck.append(substr)
                    continue
        return len(s)

if __name__ == "__main__":
    s = "ccdaabcdbb"
    dict = ["ab", "cd"]
    print Solution().minLength(s, dict)