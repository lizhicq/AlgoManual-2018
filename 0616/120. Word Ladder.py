class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, wordSet):
        import collections
        wordSet.add(end)
        wordLen = len(start)
        deck = collections.deque()
        deck.append((start, 1))
        char_list = [chr(ord('a') + i) for i in range(26)]
        while deck:
            curWord, curLen = deck.popleft()
            if curWord == end:
                return curLen
            for i in range(wordLen):
                part1 = curWord[:i]
                part2 = curWord[i+1:]
                for ch in char_list:
                    if curWord[i] != ch:
                        nextWord = part1 + ch + part2
                        if nextWord in wordSet:
                            deck.append((nextWord, curLen+1))
                            wordSet.remove(nextWord)
        return 0

if __name__ == "__main__":
    start = "hit"
    end = "cog"
    dict = set(["hot","dot","dog","lot","log"])
    print Solution().ladderLength(start, end, dict)