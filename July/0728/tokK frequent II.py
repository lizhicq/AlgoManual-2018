class Entry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

from collections import deque, OrderedDict
class TopK:
    def __init__(self, k):
        self.k = k
        self.top_k = OrderedDict()
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
            entry = next(reversed(self.top_k))
            self.top_k.popitem()
            entry.inTop = False

    def topk(self):
        if self.k == 0 or len(self.top_k) == 0:
            return []
        results = [e for e in self.top_k]
        results.sort()
        results = [e.word for e in results]
        results.reverse()
        return results

    def addToTop(self, entry):

        if self.top_k:
            last = next(reversed(self.top_k))
            self.top_k.popitem()
            entry.inTop = True
            print last.word, entry.word
            if last < entry:
                self.top_k[entry] = 1
                self.top_k[last] = 1
            else:
                self.top_k[last] = 1
                self.top_k[entry] = 1
        else:
            self.top_k[entry] = 1

    def removeFromTop(self, entry):
        self.top_k.pop(entry)
        entry.inTop = False


if __name__ == "__main__":
    s = TopK(3)
    s.add("ba")
    s.topk()
    s.add("fe")
    s.topk()
    s.add("bd")
    s.add("bf")
    s.add("fe")
    s.topk()
    s.add("ae")
    print s.topk()