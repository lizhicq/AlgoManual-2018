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
        listA = []
        listB = []
        if headA == None or headB == None:
            return None
        while 1:
            if headA == None:
                break;
            listA.append(headA.val)
            headA = headA.next

        while 1:
            if headB == None:
                break;
            listB.append(headB.val)
            headB = headB.next

        if listA[-1] != listB[-1]:
            return None;

        if len(listA) < len(listB):
            minLen = len(listA)
        else:
            minLen = len(listB)

        inster = []
        for i in range(1, minLen + 1):
            if listA[-i] != listB[-i]:
                return ListNode(listA[-i + 1])
            if i == minLen:
                return ListNode(listA[-i])