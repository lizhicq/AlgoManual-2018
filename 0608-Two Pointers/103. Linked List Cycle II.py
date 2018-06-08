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
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return False


if __name__ == "__main__":
    # 21->10->4->5

    root = ListNode(21)
    root.next = ListNode(10)
    root.next.next = ListNode(4)
    root.next.next.next = ListNode(5)
    root.next.next.next.next = root
    print Solution().detectCycle(root).val