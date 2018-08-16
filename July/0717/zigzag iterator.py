class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        self.vecs = []
        self.turns = 0
        for vec in vecs:
            vec and self.vecs.append(iter(vec))

    """
    @return: An integer
    """
    def next(self):
        try:
            elem = self.vecs[self.turns].next()
            self.turns = (self.turns + 1) % len(self.vecs)
            return elem
        except StopIteration:
            self.elem = None
            self.vecs.pop(self.turns)
            if len(self.vecs) > 0:
                self.turns %= len(self.vecs)

    """
    @return: True if has next
    """
    def hasNext(self):
        return len(self.vecs) > 0

if __name__ == "__main__":
    s = ZigzagIterator2([[1,2],[3,4,5,6]])
    while s.hasNext():
        print s.next()

class ZigzagIterator2:

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        from collections import deque
        self.queue = deque([v for v in vecs if v])

    def next(self):
        # Write your code here
        v = self.queue.popleft()
        value = v.pop(0)
        if v:
            self.queue.append(v)
        return value

    def hasNext(self):
        # Write your code here
        return len(self.queue) > 0

if __name__ == "__main__":
    s = ZigzagIterator2([[1,2,3],[],[4,5,6]])
    while s.hasNext():
        print s.next()
