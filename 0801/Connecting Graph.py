class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.edges = {}
        for i in range(1, n+1):
            self.edges[i] = set()

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        self.edges[a].add(b)
        self.edges[b].add(a)

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        if b in self.edges[a]:
            return True
        return False