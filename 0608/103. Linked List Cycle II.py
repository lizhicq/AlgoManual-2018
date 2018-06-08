
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):







if __name__ == "__main__":
    #21->10->4->5

    root = ListNode(21)
    root.next = ListNode(10)
    root.next.next = ListNode(4)
    root.next.next.next = ListNode(5)
    root.next.next.next.next = root

