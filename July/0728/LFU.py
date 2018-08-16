from collections import OrderedDict
class LFUCache:
    def __init__(self, capacity):
        self.valuemap = {}
        self.countmap = {}
        self.freqmap = {1:OrderedDict()}
        self.CAP = capacity
        self.minFreq = 0

    def set(self, key, value):
        if key in self.valuemap:
            self.valuemap[key] = value
            self.get(key)
            return
        if len(self.valuemap) >= self.CAP:
            lowkey = next(iter(self.freqmap[self.minFreq]))
            self.freqmap[self.minFreq].popitem()
            self.valuemap.pop(lowkey)
        self.valuemap[key] = value
        self.minFreq = 1
        self.countmap[key] = 1
        self.freqmap[1][key] = 1

    def get(self, key):
        #print self.countmap, self.valuemap, self.freqmap
        if key not in self.valuemap:
            return -1
        freq = self.countmap[key]
        print freq, key, self.freqmap, self.valuemap, self.countmap
        self.freqmap[freq].pop(key)
        if freq == self.minFreq and len(self.freqmap[freq]) == 0:
            self.minFreq += 1
        freq += 1
        self.countmap[key] = freq
        if freq not in self.freqmap:
            self.freqmap[freq] = OrderedDict()
        self.freqmap[freq][key] = 1
        return self.valuemap[key]


if __name__ == "__main__":
    s = LFUCache(3)
    s.set(1, 10)
    s.set(2, 20)
    s.set(3, 30)
    s.get(1)
    s.set(4, 40)
    s.get(4)
    s.get(3)
    s.get(2)
    s.get(1)
    s.set(5, 50)
    s.get(1)
    s.get(2)
    s.get(3)
    s.get(4)
    s.get(5)