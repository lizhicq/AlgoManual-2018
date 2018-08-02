class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.father = [0 for _ in range(n+1)]

    def find(self, x):
        if self.father[x] == 0:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b