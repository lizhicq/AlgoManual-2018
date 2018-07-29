class Entry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


from bisect import bisect_left
from collections import deque
class TopK:
    def __init__(self, k):
        self.k = k
        self.top_k = {}
        self.mapping = {}

    def add(self, word):
        if self.k == 0:
            return

        if word in self.mapping:
            entry = self.mapping[word]
            if entry.inTop:
                self.removeFromTop(entry)
            entry.freq += 1
        else:
            entry = Entry(word, 1)
            self.mapping[word] = entry

        self.addToTop(entry)

        if len(self.top_k) > self.k:
            self.top_k[0].inTop = False
            self.top_k.popleft()

    def topk(self):
        if self.k == 0 or len(self.top_k) == 0:
            return []
        results = [e.word for e in self.top_k]
        results.reverse()
        return results

    def addToTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.insert(idx, entry)
        entry.inTop = True

    def removeFromTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.remove(idx)
        entry.inTop = False

if __name__ == "__main__":
    s = TopK(2)
    s.add("lint")
    s.add("code")
    s.add("code")
    print(s.top_k)