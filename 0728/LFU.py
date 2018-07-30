class LFUCache:
    def __init__(self, capacity):
        self.valuemap = {}
        self.countmap = {}
        self.freqmap = {1:[]}
        self.CAP = capacity
        self.minFreq = 0

    def set(self, key, value):
        if key in self.valuemap:
            self.valuemap[key] = value
            self.get(key)
            return
        if len(self.valuemap) >= self.CAP:
            lowkey = self.freqmap.get(self.minFreq).pop(0)
            self.valuemap.pop(lowkey)
        self.valuemap[key] = value
        self.minFreq = 1
        self.countmap[key] = 1
        self.freqmap[1].append(key)

    def get(self, key):
        #print self.countmap, self.valuemap, self.freqmap
        if key not in self.valuemap:
            return -1
        freq = self.countmap[key]
        self.freqmap[freq].remove(key)
        if freq == self.minFreq and len(self.freqmap[freq]) == 0:
            self.minFreq += 1
        freq += 1
        self.countmap[key] = freq
        if freq not in self.freqmap:
            self.freqmap[freq] = []
        self.freqmap[freq].append(key)
        return self.valuemap[key]


if __name__ == "__main__":
    s = LFUCache(3)
    s.set(2,2)
    s.set(1,1)
    print s.get(2)
    print s.get(1)
    s.set(3,3)