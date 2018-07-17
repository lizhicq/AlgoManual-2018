class WordFreq():
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            return self.word > other.word

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        from heapq import heappop, heappush
        word_freq = {}
        for word in words:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
        heap = []
        for word, freq in word_freq.iteritems():
            heappush(heap, WordFreq(word, freq))
            if len(heap) > k:
                heappop(heap)
        ans = []
        while heap:
            word = heappop(heap).word
            ans.append(word)
        ans.reverse()
        return ans



if __name__ == "__main__":

    words = ["yes","lint","code","yes","code","baby","you",
             "baby","chrome","safari","lint","code","body",
             "lint","code"]

    s = Solution()
    print s.topKFrequentWords(words, 3)
