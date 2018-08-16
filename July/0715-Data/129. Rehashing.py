class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node 0of linked list which have twice size
    """
    def rehashing(self, hashTable):
        HASH_SIZE = 2 * len(hashTable)
        anshashTable = [None for i in range(HASH_SIZE)]
        for item in hashTable:
            p = item
            while p:
                self.addnode(anshashTable, p.val)
                p = p.next

        return hashTable

    def addlistnode(self, node, number):
        if node.next:
            self.addlistnode(node.next, number)
        else:
            node.next = ListNode(number)

    def addnode(self, anshashTable, number):
        p = number % len(anshashTable)
        if anshashTable[p] is None:
            anshashTable[p] = ListNode(number)
        else:
            self.addlistnode(anshashTable[p], number)


if __name__ == "__main__":
    s = Solution()
