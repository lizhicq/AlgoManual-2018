class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.vals = {} # key -> value
        self.prev = {} # key -> prev
        self.capacity = capacity
        self.head = ListNode(-1)
        self.tail = self.head
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if len(self.vals) < self.capacity:
            print self.tail.val
            self.vals[key] = value
            node = ListNode(key)
            node.next = self.head.next
            self.head.next = node
            self.prev[key] = self.head
            if node.next:
                self.prev[node.next.val] = node
            if len(self.vals) == self.capacity:
                p = self.head
                while p.next:
                    p = p.next
                self.tail = self.prev[p]
                
        else: # kick out tail.next key
            kick_key = self.tail.next.val
            self.vals.pop(kick_key)
            self.prev.pop(kick_key)

            node = ListNode(key)
            node.next = self.head.next
            self.head.next = node
            self.prev[node] = self.head
            self.prev[node.next] = self.node

            self.tail = self.prev[self.tail]

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key in self.vals:
            # swith key to head
            prev = self.prev[key]
            if prev is self.head:
                return self.vals[key]
            else:
                node = prev.next
                prev.next = node.next
                if node.next:
                    self.prev[node.next.val] = prev

                self.prev[self.head.next] = node
                node.next = self.head.next.next
                self.head.next = node
                self.prev[node] = self.head
                return self.vals[key]
        else:
            return -1

if __name__ == "__main__":
    s = LFUCache(3)
    s.set(1, 10)
    s.set(2, 20)
    s.set(3, 30)
    print s.get(1)
    s.set(4, 40)
    print s.get(4)
    print s.get(3)
    print s.get(2)
    print s.get(1)
