import random
class LoadBalancer:
    def __init__(self):
        self.servers = set()
        """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        self.servers.add(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        self.servers.remove(server_id)

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        return random.choice(list(self.servers))


if __name__ == "__main__":
    s = LoadBalancer()
    s.add(1)
    s.add(2)
    s.add(3)
    for i in range(100):
        print s.pick()


