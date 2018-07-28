class wordFreq(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __cmp__(self, other):
        if self.freq == other.freq:
            if self.word < other.word:
                return 1
            else:
                return -1
        return self.freq - other.freq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        if k == 0:
            return []
        from collections import Counter
        from heapq import heappop, heappush
        count = Counter(words)
        heap = []
        for word, freq in count.iteritems():
            num = wordFreq(word, freq)
            if len(heap) < k:
                heappush(heap, num)
            else:
                if heap[0] < num:
                    heappop(heap)
                    heappush(heap, num)

        ans = sorted(heap, reverse=True)
        ans = [a.word for a in ans]
        return ans


if __name__ == "__main__":
    words = ["yes", "lint", "code", "yes", "code", "baby", "you",
             "baby", "chrome", "safari", "lint", "code", "body",
             "lint", "code"]

    s = Solution()
    print s.topKFrequentWords(words, 3)
