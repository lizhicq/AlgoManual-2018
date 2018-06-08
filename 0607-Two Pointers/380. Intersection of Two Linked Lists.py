# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        lenA, lenB = 0, 0
        node1, node2 = headA, headB
        while node1 is not None:
            lenA += 1
            node1 = node1.next
        while node2 is not None:
            lenB += 1
            node2 = node2.next

        node1, node2 = headA, headB
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1
        while lenB > lenA:
            node2 = node2.next
            lenB -= 1
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1


print Solution().getIntersectionNode(None, None)