class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        from collections import deque
        from sys import maxsize
        deck = deque()
        deck.append(start)
        record = {word}
        while len(deck) > 0:
            word = deck.popleft()
            for new_word in dict:
                if len(set(word) - set(new_word)) == 1:
                    if record[new_word] < record[word] + 1:

