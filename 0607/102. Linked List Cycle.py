"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                return False
            elif fast == slow:
                return True
        return False