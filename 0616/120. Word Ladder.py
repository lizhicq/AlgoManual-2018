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
        record = {word:maxsize for word in dict}
        record[start] = 1
        record[end] = maxsize
        def check(word, new_word):
            count = 0
            for i in range(len(word)):
                if word[i] != new_word[i]:
                    count += 1
                if count > 1:
                    break
            return count == 1

        while len(deck) > 0:
            word = deck.popleft()
            for new_word in record:
                if check(word, new_word):
                    if record[new_word] > record[word] + 1:
                        record[new_word] = record[word] + 1
                        deck.append(new_word)
        print record
        return record[end]

if __name__ == "__main__":
    start = 'kiss'
    end = 'tusk'
    dict = ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]
    print Solution().ladderLength(start, end, dict)